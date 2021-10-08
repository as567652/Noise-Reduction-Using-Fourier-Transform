from operator import truediv
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import math

# getting original image and showing it
img = cv.imread('Reference_Image/original_noisy_image.tif', 0)

plt.figure()
plt.title('Original Image')
plt.imshow(img, cmap = 'gray')
plt.xticks([])
plt.yticks([])
plt.show()

# getting dft of original image
dft = cv.dft(np.float32(img),flags = cv.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20 * np.log(cv.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

# fun to tell whether a point is availaible inside circle of radius 'radius'
def dis(a, b, radius):
    tmp = (magnitude_spectrum.shape[0] // 2 - a) ** 2 + (magnitude_spectrum.shape[1] // 2 - b) ** 2
    tmp = round(math.sqrt(tmp))
    if tmp <= radius:
        return True
    else:
        return False

# showing spectrum image
plt.figure()
plt.title('Spectrum Image')
plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.xticks([])
plt.yticks([])
plt.show()

# creating mask
rows, cols = img.shape
mask = np.zeros((rows,cols,1),np.uint8)

# getting values pixel by pixel 
# if pixel value > 210 change it to 30
for i in range(len(magnitude_spectrum)):
    for j in range(len(magnitude_spectrum[0])):
        if not dis(i, j, 45):
            if magnitude_spectrum[i][j] >= 210:
                magnitude_spectrum[i][j] = 30
        mask[i][j] = min(magnitude_spectrum[i][j], 255)

# showing mask
plt.figure()
plt.title('Mask')
plt.imshow(mask, cmap = 'gray')
plt.xticks([])
plt.yticks([])
plt.show()

# multiplying mask and dft of original image
fshift = (dft_shift * mask)

# applying inverse dft to get modified image
f_ishift = np.fft.ifftshift(fshift)
img_back = cv.idft(f_ishift)
img_back = cv.magnitude(img_back[:,:,0],img_back[:,:,1])

# showing modified image
plt.figure()
plt.title('Modified Image')
plt.imshow(img_back, cmap = 'gray')
plt.xticks([])
plt.yticks([])
plt.show()