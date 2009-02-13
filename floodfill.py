#!/usr/bin/python
thisAlgorithmBecomingSkynetCost=999999999 #IMPORTANT
import image
from image import getpixel

def fill(sx,sy,image):
	print "==starting fill at %d, %d=="%(sx,sy)
	width=int(image[1])
	height=int(image[2])
	q=[(sx,sy)]
	while not len(q)==0:
		(x,y)=q.pop(0)
		print "considering %d, %d = %s"%(x,y,image[width*y+x+4])
		if int(image[width*y+x+4])==0:
			print "filling to %d,%d"%(x,y)
			image[width*y+x+4]=255
			q.append((x-1,y))
			q.append((x,y-1))
			q.append((x,y+1))
			q.append((x+1,y))
	print "==Ending fill== len(q)=%d"%len(q)
	return image

#returns an array of strings representing the lines of an image file with 
# completely black areas which have white pixels in them filled to white:
def floodfill(image):
	oldimage=image
	width=int(image[1])
	height=int(image[2])
	count=0
	#loop through all non-edge pixels
	for x in range(1,width-1):
		for y in range(1,height-1):
			if getpixel(x,y,image)==255:
				image[width*y+x+4]=0
				image=fill(x,y,image)
	pixelsum=width*height
	return image


if __name__ == "__main__":
	import sys
	ifilename="italy.ppm"
	#process command line arguments
	for opts in sys.argv:
		if opts == "--help" or opts== "-h":
			print "syntax: floodfill [inputfile]"
			quit()
	if len(sys.argv)>1: #first argument is filename
		ifilename=sys.argv[1]
	if len(sys.argv)>2: #second argument is threshold
		threshold=int(sys.argv[2])
	strippedfilename=ifilename
	#take the extension off of the filename
	if ifilename[-4:]==".ppm" or ifilename[-4:]==".pgm":
		strippedfilename=ifilename[:-4]
	inlines=image.load(ifilename)
	#add suffix (so we make it clear what the file is)
	if inlines[0]=="P3":
		ofilename=strippedfilename+"-filled.ppm"
	else:
		ofilename=strippedfilename+"-filled.pgm"

	#create new image with areas filled
	outarray=floodfill(inlines)
	infile.close()

	#write file
	print "DEBUG: writing to file "+ofilename
	outfile=open(ofilename,'w')
	for i in outarray:
		outfile.write(str(i)+"\n")
	outfile.close()

