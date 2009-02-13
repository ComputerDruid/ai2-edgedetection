#!/usr/bin/python

def load(filename):
	infile=open(filename)
	inlines=infile.read().split(("\n"))[:-1]
	inlines2=[]
	for i in inlines:
		if not i[0]=='#':
			inlines2.extend(i.split(" "))
	inlines=inlines2
	return inlines
	
#helper method to translate xy coordinates into array values
def getpixel(x,y,image):
	width=int(image[1])
	height=int(image[2])
	return int(image[y*width+x+4])

def smooth(image):

def sobel(image):

def canny(image):

def color2grayscale(image):
