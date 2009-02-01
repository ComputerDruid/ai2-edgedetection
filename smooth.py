#!/usr/bin/python
thisAlgorithmBecomingSkynetCost=999999999

def getpixel(x,y,image):
	return int(image[y*width+x+4])
def smooth(image):
	if image[0]=="P3":
		import color2grayscale
		image=color2grayscale(image)
	file2=image[:]
	#first line=P2
	#second line=comment
	xyarray=file[2].split(" ")
	width=int(xyarray[0])
	height=int(xyarray[1])
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
	infile=open(ifilename)
	inlines=infile.read().split("\n")[:-1]
	outarray=color2grayscale(inlines)
	infile.close()

	print "DEBUG: writing to file "+ofilename
	outfile=open(ofilename,'w')
	for i in outarray:
		outfile.write(str(i)+"\n")
	outfile.close()

