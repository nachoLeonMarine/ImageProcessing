from skimage import io
import pandas as pd
img = io.imread ('images/horario.jpg')
df = pd.DataFrame(img.flatten())
filepath = 'pixel_values.xlsx'
df.to_excel(filepath, index=False)
