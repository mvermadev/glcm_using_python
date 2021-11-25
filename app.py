from os import linesep
from flask import Flask, escape, request
import numpy as np
from skimage.feature import greycomatrix, greycoprops
from skimage import io, color, img_as_ubyte

app = Flask(__name__)

img = io.imread('myImage.jpg')

gray = color.rgb2gray(img)
image = img_as_ubyte(gray)

bins = np.array([0, 16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240, 255]) #16-bit
inds = np.digitize(image, bins)

max_value = inds.max()+1
matrix_coocurrence = greycomatrix(inds, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4], levels=max_value, normed=False, symmetric=False)


# GLCM properties
def contrast_feature(matrix_coocurrence):
	contrast = greycoprops(matrix_coocurrence, 'contrast')
	f = open("file.txt", "w")
	str_dictionary = repr(contrast)
	f.write("contrast = " + str_dictionary + "\n")
	return "Contrast = ", contrast

def dissimilarity_feature(matrix_coocurrence):
	dissimilarity = greycoprops(matrix_coocurrence, 'dissimilarity')	
	f = open("file.txt", "a")
	str_dictionary = repr(dissimilarity)
	f.write("Dissimilarity = " + str_dictionary + "\n")
	return "Dissimilarity = ", dissimilarity

def homogeneity_feature(matrix_coocurrence):
	homogeneity = greycoprops(matrix_coocurrence, 'homogeneity')
	f = open("file.txt", "a")
	str_dictionary = repr(homogeneity)
	f.write("Homogeneity = " + str_dictionary + "\n")
	return "Homogeneity = ", homogeneity

def energy_feature(matrix_coocurrence):
	energy = greycoprops(matrix_coocurrence, 'energy')
	f = open("file.txt", "a")
	str_dictionary = repr(energy)
	f.write("Energy = " + str_dictionary + "\n")
	return "Energy = ", energy

def correlation_feature(matrix_coocurrence):
	correlation = greycoprops(matrix_coocurrence, 'correlation')
	f = open("file.txt", "a")
	str_dictionary = repr(correlation)
	f.write("Correlation = " + str_dictionary + "\n")
	return "Correlation = ", correlation

def asm_feature(matrix_coocurrence):
	asm = greycoprops(matrix_coocurrence, 'ASM')
	f = open("file.txt", "a")
	str_dictionary = repr(asm)
	f.write("ASM = " + str_dictionary + "\n")
	return "ASM = ", asm

print(contrast_feature(matrix_coocurrence))
print(dissimilarity_feature(matrix_coocurrence))
print(homogeneity_feature(matrix_coocurrence))
print(energy_feature(matrix_coocurrence))
print(correlation_feature(matrix_coocurrence))
print(asm_feature(matrix_coocurrence))

	
def something():
	f = open("file.txt", "r")
	return f.read().format(linesep)

@app.route('/')
@app.route('/home')
def home():
	return something()


if __name__ == "__main__":
	app.secret_key = "ItIsASecret"
	app.debug = True
	app.run()