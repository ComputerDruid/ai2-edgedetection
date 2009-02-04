#!/usr/bin/python
thisAlgorithmBecomingSkynetCost=999999999
threshold=255
def getpixel(x,y,image):
	xyarray=image[2].split(" ")
	width=int(xyarray[0])
	height=int(xyarray[1])
	return int(image[y*width+x+4])
def edgedetect(image):
	oldimage=image
	if image[0]=="P3":
		import smooth
		image=smooth.smooth(image)
	file2=oldimage[:]
	#first line=P2
	#second line=comment
	xyarray=image[2].split(" ")
	width=int(xyarray[0])
	height=int(xyarray[1])
	count=0
	for x in range(1,width-1):
		for y in range(1,height-1):
			hg=int(-1*getpixel(x-1,y-1,image)+0*getpixel(x,y-1,image)+1*getpixel(x+1,y-1,image)-2*getpixel(x-1,y,image)+0*getpixel(x,y,image)+2*getpixel(x+1,y,image)-1*getpixel(x-1,y+1,image)+0*getpixel(x,y+1,image)+1*getpixel(x+1,y+1,image))
			vg=int(1*getpixel(x-1,y-1,image)+2*getpixel(x,y-1,image)+1*getpixel(x+1,y-1,image)+0*getpixel(x-1,y,image)+0*getpixel(x,y,image)+0*getpixel(x+1,y,image)-1*getpixel(x-1,y+1,image)-2*getpixel(x,y+1,image)-1*getpixel(x+1,y+1,image))
			if(abs(hg)+abs(vg)>threshold):
				if oldimage[0]=="P3":
					file2[(width*y+x)*3+4]=255
					file2[(width*y+x)*3+5]=0
					file2[(width*y+x)*3+5]=0
				else:
					file2[width*y+x+4]=255
	return file2
if __name__ == "__main__":
	import sys
	ifilename="italy-smoothed.pgm"
	for opts in sys.argv:
		if opts == "--help" or opts== "-h":
			print "syntax: edgedetect [inputfile] [threshold]"
			quit()
	if len(sys.argv)>1:
		ifilename=sys.argv[1]
	if len(sys.argv)>2:
		threshold=int(sys.argv[2])
	strippedfilename=ifilename
	if ifilename[-4:]==".ppm" or ifilename[-4:]==".pgm":
		strippedfilename=ifilename[:-4]
	infile=open(ifilename)
	inlines=infile.read().split("\n")[:-1]
	if inlines[0]=="P3":
		ofilename=strippedfilename+"-edges-"+str(threshold)+".ppm"
	else:
		ofilename=strippedfilename+"-edges-"+str(threshold)+".pgm"
	outarray=edgedetect(inlines)
	infile.close()

	print "DEBUG: writing to file "+ofilename
	outfile=open(ofilename,'w')
	for i in outarray:
		outfile.write(str(i)+"\n")
	outfile.close()

