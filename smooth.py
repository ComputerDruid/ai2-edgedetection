#!/usr/bin/python
thisAlgorithmBecomingSkynetCost=999999999
from image import getpixel,load

def smooth(image):
	print "smooth: "+str(image[:10])
	if image[0]=="P3":
		import color2grayscale
		image=color2grayscale.color2grayscale(image)
	print "smooth: "+str(image[:10])
	file2=image[:]
	#first line=P2
	#second line=comment
	width=int(image[1])
	height=int(image[2])
	count=0
	for x in range(1,width-1):
		for y in range(1,height-1):
			file2[width*y+x+4]=int((1*getpixel(x-1,y-1,image)+2*getpixel(x,y-1,image)+1*getpixel(x+1,y-1,image)+2*getpixel(x-1,y,image)+4*getpixel(x,y,image)+2*getpixel(x+1,y,image)+1*getpixel(x-1,y+1,image)+2*getpixel(x,y+1,image)+1*getpixel(x+1,y+1,image))/16)
	return file2
if __name__ == "__main__":
	import sys
	ifilename="italy.pgm"
	for opts in sys.argv:
		if opts == "--help" or opts== "-h":
			print "syntax: smooth [inputfile]"
			quit()
	if len(sys.argv)>1:
		ifilename=sys.argv[1]
	strippedfilename=ifilename
	if ifilename[-4:]==".ppm" or ifilename[-4:]==".pgm":
		strippedfilename=ifilename[:-4]
	ofilename=strippedfilename+"-smoothed.pgm"
	inlines=load(ifilename)
	outarray=smooth(inlines)

	print "DEBUG: writing to file "+ofilename
	outfile=open(ofilename,'w')
	for i in outarray:
		outfile.write(str(i)+"\n")
	outfile.close()

