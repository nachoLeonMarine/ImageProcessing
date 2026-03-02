from skimage import io
from skimage import draw
import matplotlib.pyplot as plt

img = io.imread ('images/islas_cies.jpg')
def rectangle (x,y,w,h,shape):
    rr,cc = [x, x + w, x + w, x ], [y, y, y + h, y + h]
    return (draw.polygon(rr,cc, shape = shape))

rr, cc = rectangle (1000,2000,500,500 ,shape = img.shape)
img [rr,cc] = 255

xx, yy = draw.circle_perimeter (500,500,100)
img [xx,yy] = 255


plt.imshow(img)
plt.show()
