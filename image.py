#!/usr/bin/python
import math

def load(filename):
	infile=open(filename)
	inlines=infile.read().split(("\n"))[:-1]
	inlines2=[]
	for i in inlines:
		if not i[0]=='#':
			inlines2.extend(i.split(" "))
	inlines=inlines2
	infile.close()
	return inlines
	
#helper method to translate xy coordinates into array values
def getpixel(x,y,image):
	width=int(image[1])
	height=int(image[2])
	return int(image[y*width+x+4])
def getpixfromdir(x,y,theta):
	i=int((theta+math.pi/8)/math.pi*4)%8
	if i==0:
		return (x+1,y)
	elif i==1:
		return (x+1,y+1)
	elif i==2:
		return (x,y+1)
	elif i==3:
		return (x-1,y+1)
	elif i==4:
		return (x-1,y)
	elif i==5:
		return (x-1,y-1)
	elif i==6:
		return (x,y-1)
	else:
		return (x+1,y-1)

#def smooth(image):

#def sobel(image):

#def canny(image):

#def color2grayscale(image):
