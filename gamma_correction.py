from skimage import exposure
from skimage import io
from pylab import *
import matplotlib.pyplot as plt


img = io.imread('images/islas_cies.jpg')

gamma_corrected1 = exposure.adjust_gamma (img, 0.5)
gamma_corrected2 = exposure.adjust_gamma (img, 5)

figure (0)
plt.imshow(gamma_corrected1)
plt.show()


figure (1)
plt.imshow(gamma_corrected2)
plt.show()


