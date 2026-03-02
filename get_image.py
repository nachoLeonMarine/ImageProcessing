from skimage import io
import matplotlib.pyplot as plt

img = io.imread ('images/caleta1.jpg')
#io.imshow(img)
# Replace io.imshow(img) with:
plt.imshow(img)
plt.show()


print ('Image Resolution: ', img.shape)
