# Super Resolution on Astronomical images

## About
* Trained a deep learning model based on GANs to upscale the astronomical images (4X)
* Used tensorflow keras to implement a mini residual CNN architecture

## Give it a try

* Copy SRGAN_model.ipynb and gen_weight_final.h5 to your drive
* Open <a href="https://colab.research.google.com/">Google Colab</a> and run the SRGAN_model.ipynb
* Call showImages with input image path as argument. Your results are out!

## Issues

* Current model blurs the areas of high frequency.
* Output images are having low contrast as compared to target images.
* The model produces random noise in some cases. 


## Future Work include

* Fine tune current model to achieve better results.
* Training on larger and diverse dataset.
* Trying different architectures and hyper-parameters.

## Results

<img src="https://github.com/dakshverma2411/super-resolution-on-astronomical-images/blob/master/Results/demo1.jpg" alt="alt text" width="2048" height="360">

<img src="https://github.com/dakshverma2411/super-resolution-on-astronomical-images/blob/master/Results/demo2.jpg" alt="alt text" width="2048" height="360">

<img src="https://github.com/dakshverma2411/super-resolution-on-astronomical-images/blob/master/Results/demo3.jpg" alt="alt text" width="2048" height="360">

<img src="https://github.com/dakshverma2411/super-resolution-on-astronomical-images/blob/master/Results/demo4.jpg" alt="alt text" width="2048" height="360">

<img src="https://github.com/dakshverma2411/super-resolution-on-astronomical-images/blob/master/Results/demo5.jpg" alt="alt text" width="2048" height="360">

<img src="https://github.com/dakshverma2411/super-resolution-on-astronomical-images/blob/master/Results/demo6.jpg" alt="alt text" width="2048" height="360">

## Resources

* Paper - https://arxiv.org/pdf/1609.04802.pdf
* Dataset - https://esahubble.org/images/
* Trained on - https://colab.research.google.com/
