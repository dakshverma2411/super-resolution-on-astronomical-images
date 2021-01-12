import urllib.request as urllib
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

def getHtml(url):
    response=urllib.urlopen(url)
    page=response.read().decode('utf-8')
    return page

def getData(page):
    parsedHtml=BeautifulSoup(page,features='lxml')
    data=parsedHtml.find('script').text
    return data

def getLinks(data):
    lines=data.split('\n')
    links=[]
    for i in lines:
        if(i[:3]=='src'):
            links.append(i[5:-2])
    return links

def imageLinks():
    base_url='https://esahubble.org/images/page/'
    links=[]
    for i in range(2,18):
        url=base_url+str(i)+'/'
        page=getHtml(url)
        data=getData(page)
        data=data.replace(' ','')
        links.extend(getLinks(data))

    url2='https://esahubble.org/images/'
    page=getHtml(url2)
    data=getData(page)
    data=data.replace(' ','')
    links.extend(getLinks(data))
    return links


linksFinal=imageLinks()
print(len(linksFinal),'links found.')
with open('links.txt','w') as f:
    for i in linksFinal:
        f.write(i+'\n')
    print('Links saved in links.txt')
