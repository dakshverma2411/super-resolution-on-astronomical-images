import urllib.request
# import only system from os 
from os import system, name 
  
# import sleep to show output for some time period 
from time import sleep 

def download(url):
    name=url.split('/')[-1]
    urllib.request.urlretrieve(url,name)

with open('links.txt','r') as f:
    string=f.read()
    links=string.split('\n')
    print(len(links),' images to download')
    for i,imgurl in enumerate(links[651:]):
        download(imgurl)
        if(i%50==0):
            print(f'{i} images downloaded.')