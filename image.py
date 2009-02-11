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
def smooth(image):

def sobel(image):

def canny(image):

def color2grayscale(image):
