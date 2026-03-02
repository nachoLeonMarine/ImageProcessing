from skimage import io
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
from skimage  import transform
from pylab import *

img1 = io.imread('images/tanker_guadalquivir.jpg')
img2 = io.imread('images/essaouira.jpg')
img2 = transform.resize(img2, img1.shape)

#ssim_1 = ssim (img1, img2, data_range = img2.max() - img2.min(), multichannel = True )
ssim_1 = ssim (img1, img2, channel_axis=-1, data_range= 1.0)

figure (0)
plt.imshow(img1)
plt.show()

figure (1)
plt.imshow(img2)
plt.show()

print ('SSIM factor: ', ssim_1)


