#import libraries

from skimage import io
from skimage import color
from skimage import data
from skimage import util
from pylab import *
import matplotlib.pyplot as plt
import numpy as np


#read image
img = io.imread('images/fruits.jpg')

#convert to HSV
img_hsv = color.rgb2hsv(img)

#print ('Original Colour')
figure(0)
plt.imshow(img)
plt.show()

figure(1)
plt.imshow(img_hsv)
plt.show()

# Convert safely to 8-bit unsigned integer
img_hsv2 = util.img_as_ubyte(img_hsv)
io.imsave("images/fruits_hsv.jpg", img_hsv2)

figure(2)
plt.imshow(img_hsv2)
plt.show()



