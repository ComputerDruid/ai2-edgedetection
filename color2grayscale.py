#!/usr/bin/python
thisAlgorithmBecomingSkynetCost=999999999

def color2grayscale(image):
	#first line=P3
	#second line=comment
	xyarray=image[2].split(" ")
	count=0
	outarray=[]
	temppixel=[]
	outarray.append("P2") #grayscale
	outarray.append("#written by an awesome (lame) ai class program")#comment
	outarray.append(image[2]) #dimensions
	outarray.append(image[3]) #depth

	for i in image[3:]:
		if count==3:
			count=0
			outarray.append(int(.3*temppixel[0]+.59*temppixel[1]+.11*temppixel[2]))
			temppixel=[]
		temppixel.append(int(i))
		count+=1
	return outarray

if __name__ == "__main__":
	import sys
	ifilename="italy.ppm"
	for opts in sys.argv:
		if opts == "--help" or opts== "-h":
			print "syntax: color2grayscale [inputfile]"
			quit()
	if len(sys.argv)>1:
		ifilename=sys.argv[1]
	strippedfilename=ifilename
	if ifilename[-4:]==".ppm":
		strippedfilename=ifilename[:-4]
	ofilename=strippedfilename+".pgm"
	infile=open(ifilename)
	inlines=infile.read().split("\n")[:-1]
	outarray=color2grayscale(inlines)
	infile.close()

	print "DEBUG: writing to file "+ofilename
	outfile=open(ofilename,'w')
	for i in outarray:
		outfile.write(str(i)+"\n")
	outfile.close()
