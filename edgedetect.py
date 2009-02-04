#!/usr/bin/python
thisAlgorithmBecomingSkynetCost=999999999 #IMPORTANT

threshold=255 #default threshold if not specified on the command line

#count the number of pixels marked as edges
pixelcount=0
pixelnum=0

#helper method to translate xy coordinates into array values
def getpixel(x,y,image):
	xyarray=image[2].split(" ")
	width=int(xyarray[0])
	height=int(xyarray[1])
	return int(image[y*width+x+4])

#returns an array of strings representing the lines of an image file with 
#edge pixels marked according to sobel's method.
def edgedetect(image):
	global pixelsum, pixelcount
	oldimage=image
	if image[0]=="P3":
		#converts file to grayscale and smoothes it
		import smooth
		image=smooth.smooth(image)
	file2=oldimage[:]
	xyarray=image[2].split(" ")
	width=int(xyarray[0])
	height=int(xyarray[1])
	count=0
	#loop through all non-edge pixels
	for x in range(1,width-1):
		for y in range(1,height-1):
			#calculate the horizontal gradient of the current pixel
			hg=int(-1*getpixel(x-1,y-1,image)+0*getpixel(x,y-1,image)+1*getpixel(x+1,y-1,image)-2*getpixel(x-1,y,image)+0*getpixel(x,y,image)+2*getpixel(x+1,y,image)-1*getpixel(x-1,y+1,image)+0*getpixel(x,y+1,image)+1*getpixel(x+1,y+1,image))
			#calculate the vertical gradient of the current pixel
			vg=int(1*getpixel(x-1,y-1,image)+2*getpixel(x,y-1,image)+1*getpixel(x+1,y-1,image)+0*getpixel(x-1,y,image)+0*getpixel(x,y,image)+0*getpixel(x+1,y,image)-1*getpixel(x-1,y+1,image)-2*getpixel(x,y+1,image)-1*getpixel(x+1,y+1,image))
			#if the threshold is reached, mark the pixel
			if(abs(hg)+abs(vg)>threshold):
				#count the number of pixels marked as edges
				pixelcount+=1
				if oldimage[0]=="P3": #image is color, mark as red
					file2[(width*y+x)*3+4]=255
					file2[(width*y+x)*3+5]=0
					file2[(width*y+x)*3+5]=0
				else: #image is grayscale, mark as white
					file2[width*y+x+4]=255
	pixelsum=width*height
	return file2
if __name__ == "__main__":
	import sys
	ifilename="italy.ppm"
	#process command line arguments
	for opts in sys.argv:
		if opts == "--help" or opts== "-h":
			print "syntax: edgedetect [inputfile] [threshold]"
			quit()
	if len(sys.argv)>1: #first argument is filename
		ifilename=sys.argv[1]
	if len(sys.argv)>2: #second argument is threshold
		threshold=int(sys.argv[2])
	strippedfilename=ifilename
	#take the extension off of the filename
	if ifilename[-4:]==".ppm" or ifilename[-4:]==".pgm":
		strippedfilename=ifilename[:-4]
	infile=open(ifilename)
	inlines=infile.read().split("\n")[:-1]
	#add suffix (so we make it clear what the file is)
	if inlines[0]=="P3":
		ofilename=strippedfilename+"-edges-"+str(threshold)+".ppm"
	else:
		ofilename=strippedfilename+"-edges-"+str(threshold)+".pgm"

	#create new image with edge pixels marked
	outarray=edgedetect(inlines)
	infile.close()

	#write file
	print "DEBUG: writing to file "+ofilename
	outfile=open(ofilename,'w')
	for i in outarray:
		outfile.write(str(i)+"\n")
	outfile.close()
	print "%d/%d pixels detected as edges"%(pixelcount,pixelsum)

