#!/usr/bin/python
thisAlgorithmBecomingSkynetCost=999999999 #IMPORTANT

#helper method to translate xy coordinates into array values
def getpixel(x,y,image):
	width=int(image[1])
	height=int(image[2])
	return int(image[y*width+x+4])


def invert(image):
	width=int(image[1])
	height=int(image[2])
	count=0
	#loop through all non-edge pixels
	for x in range(1,width-1):
		for y in range(1,height-1):
			if getpixel(x,y,image)==255:
				image[width*y+x+4]=0
			else:
				image[width*y+x+4]=255
	pixelsum=width*height
	return image


if __name__ == "__main__":
	import sys
	ifilename="italy-smoothed-edges.pgm"
	#process command line arguments
	for opts in sys.argv:
		if opts == "--help" or opts== "-h":
			print "syntax: invert [inputfile]"
			quit()
	if len(sys.argv)>1: #first argument is filename
		ifilename=sys.argv[1]
	if len(sys.argv)>2: #second argument is threshold
		threshold=int(sys.argv[2])
	strippedfilename=ifilename
	#take the extension off of the filename
	if ifilename[-4:]==".ppm" or ifilename[-4:]==".pgm":
		strippedfilename=ifilename[:-4]
	import image
	inlines=image.load(ifilename)
	#add suffix (so we make it clear what the file is)
	if inlines[0]=="P3":
		ofilename=strippedfilename+"-inverted.ppm"
	else:
		ofilename=strippedfilename+"-inverted.pgm"

	#create new image with areas filled
	outarray=invert(inlines)

	#write file
	print "DEBUG: writing to file "+ofilename
	outfile=open(ofilename,'w')
	for i in outarray:
		outfile.write(str(i)+"\n")
	outfile.close()

