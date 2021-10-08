# Noise Reduction Using Fourier Transform
Implementating Case Specific Noise Reduction using Discrete Fourier Transform (DFT).


## Table of contents
* [Introduction](#introduction)
* [Approach](#approach)
* [Technologies](#technologies)
* [Setup](#setup)
* [Launch](#launch)
* [Illustrations](#illustrations)
* [Status](#status)
* [Sources](#sources)
* [Other](#other)


## Introduction
General method to remove Periodic Noise is by using different type of filters. This technique is generally called **Periodoc Noise Reduction by Frequency Domain Filtering**. Different filters that can be used to remove periodic noise are 
- Bandreject Filter 
- Bandpass Filter
- Notch Filter and many more.
If Noise is periodic, we can simply use any of the above filters to minimize noise content in the image.
If noise is not periodic than manually we need to remove noise. Important note here is that first we have to change Spatial Domain into frequency Domain, to apply filter.


## Approach
- To change spatial domain into frequency domain first we apply **Discrete Fourier Transform (DFT)** on the image.
- Now we are able to see spectrum of the image.
- We can see that there is not a pattern here that we can follow to remove noise.
- We just create a mask of spectrum image in such a way that central light burst is there. Others are blacked out.
- We adjust radius of central burst that is needed to be left out.
- We than multiply mask and DFT (Discrete Fourier Transform)
- We apply **IDFT (Inverse Discrete Fourier Transform)** to obtain modified Image


## Technologies
  #### Software Used :
  * VS Code : 1.58.2
  #### Languages Used :
  * Python 3
  #### OS used :
  * Ubuntu 20.04.3 LTS 64-bit


## Setup
First you must have these libraries and languages installed on your system -
  * [Python 3](https://www.python.org/)
  * [OpenCV](https://opencv.org/)


## Launch
To run the code, run this commands in terminal with main.py as in current directory and images in Images folder along with main.py
```
$ python3 main.py
```
Windows will pop-up with resultant images. (Press **X** to view next image).


## Illustrations
### Step By Step Image Transformation For Noise Reduction
<p align="center">
  <img src="ReadMe_Images/Original_Image.png" width=48% title="Original Image">
  <img src="ReadMe_Images/Spectrum.png" width=48% title="Spectrum Of Original Image">
</p>
<p align="center">
  <img src="ReadMe_Images/Mask.png" width=48% title="Mask">
  <img src="ReadMe_Images/Modified_Image.png" width=48% title="Modified Image">
</p>


## Project status
  ***Completed***


## Sources
  * Images used in this project may be subject to copyright.
  * [Digital Image Processing (Third Edition) by Rafael C. Gonzalez and Richard E. Woods](https://www.amazon.com/Digital-Image-Processing-Rafael-Gonzalez/dp/013168728X)
  * [OpenCV Documentation](https://docs.opencv.org/2.4/opencv_tutorials.pdf)
  
  
## Other
  This code was contributed by Abhinav Sharma.
