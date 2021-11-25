from skimage.feature import greycomatrix
from skimage import io
import numpy as np 

image = io.imread('myImage.jpg')
max_value = image.max()

matrix_coocurrence = greycomatrix(image, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4], levels=max_value+1, normed=False, symmetric=False)

print(matrix_coocurrence[:,:,0,0])
print(matrix_coocurrence[:,:,0,1])
print(matrix_coocurrence[:,:,0,2])
print(matrix_coocurrence[:,:,0,3])
