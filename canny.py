#!/usr/bin/python
thisAlgorithmBecomingSkynetCost=999999999 #IMPORTANT

from math import atan2
import math
from image import getpixel,load,getpixfromdir

lthreshold=200 #default lower threshold if not specified on the command line
hthreshold=400 #default higher threshold if not specified on the command line

#count the number of pixels marked as edges
pixelcount=0
pixelnum=0

#helper method to translate xy coordinates into array values

def fill(sx, sy, image, tvals, theta, threshold):
	global pixelcount
	print "=starting fill at %d, %d="%(sx,sy)
	width=int(image[1])
	height=int(image[2])
	q=[(sx,sy)]
	while not len(q)==0:
		(x,y)=q.pop(0)
		try:
			print "considering %d, %d = %s"%(x,y,tvals[width*y+x+4])
			if int(tvals[width*y+x+4])>threshold:
				#(x1,y1)=getpixfromdir(x,y,float(theta[width*y+x+4])+math.pi/2)
				#(x2,y2)=getpixfromdir(x,y,float(theta[width*y+x+4])+3*math.pi/2)
				(x1,y1)=getpixfromdir(x,y,float(theta[width*y+x+4]))
				(x2,y2)=getpixfromdir(x,y,float(theta[width*y+x+4])+math.pi)
				print "neighbors: %s,%s"%(str((x1,y1)),str((x2,y2)))
				if(width*y1+x1+4<0 or width*y1+x1+4>len(tvals)):
					print "bumping into edge 1"
				elif(int(tvals[width*y1+x1+4])<=int(tvals[width*y+x+4])):
					if(width*y2+x2+4<0 or width*y2+x2+4>len(tvals)):
						print "bumping into edge 2"
					elif(int(tvals[width*y2+x2+4])<=int(tvals[width*y+x+4])):
					
						print "filling to %d,%d"%(x,y)
						pixelcount+=1
						if image[0]=="P3": #image is color, mark as red
							if image[(width*y+x)*3+4]==255 and image[(width*y+x)*3+5]==0 and image[(width*y+x)*3+6]==0:
								break
							image[(width*y+x)*3+4]=255
							image[(width*y+x)*3+5]=0
							image[(width*y+x)*3+6]=0
						else:
							if image[width*y+x+4]==255:
								break
							image[width*y+x+4]=255
						q.append(getpixfromdir(x,y,float(theta[width*y+x+4])+math.pi/2))
						q.append(getpixfromdir(x,y,float(theta[width*y+x+4])+3*math.pi/2))
						#q.append((x,y+1))
						#q.append((x+1,y))
					else:
						print "(%d,%d) is better with a tval of %d"%(x2,y2,int(tvals[width*y2+x2+4]))
						q.append((x2,y2))
				else:
					print "(%d,%d) is better with a tval of %d"%(x1,y1,int(tvals[width*y1+x1+4]))
					q.append((x1,y1))
		except:
			print "oops! edge"
	print "=Ending fill= len(q)=%d"%len(q)
	return image

#returns an array of strings representing the lines of an image file with 
#edge pixels marked according to sobel's method.
def edgedetect(image):
	print image[:10]
	tvals=image[:]
	hg=image[:]
	vg=image[:]
	theta=image[:]
	global pixelsum, pixelcount
	oldimage=image
	if image[0]=="P3":
		#converts file to grayscale and smoothes it
		import smooth
		image=smooth.smooth(image)
	print image[:10]
	file2=oldimage[:]
	width=int(image[1])
	height=int(image[2])
	count=0
	#loop through all non-edge pixels
	for x in range(1,width-1):
		for y in range(1,height-1):
			#calculate the horizontal gradient of the current pixel
			hg[width*y+x+4]=int(-1*getpixel(x-1,y-1,image)+0*getpixel(x,y-1,image)+1*getpixel(x+1,y-1,image)-2*getpixel(x-1,y,image)+0*getpixel(x,y,image)+2*getpixel(x+1,y,image)-1*getpixel(x-1,y+1,image)+0*getpixel(x,y+1,image)+1*getpixel(x+1,y+1,image))
			#calculate the vertical gradient of the current pixel
			vg[width*y+x+4]=int(1*getpixel(x-1,y-1,image)+2*getpixel(x,y-1,image)+1*getpixel(x+1,y-1,image)+0*getpixel(x-1,y,image)+0*getpixel(x,y,image)+0*getpixel(x+1,y,image)-1*getpixel(x-1,y+1,image)-2*getpixel(x,y+1,image)-1*getpixel(x+1,y+1,image))
			#store the threshold value
			tvals[width*y+x+4]=abs(hg[width*y+x+4])+abs(vg[width*y+x+4])
			theta[width*y+x+4]=float(atan2(-vg[width*y+x+4],hg[width*y+x+4]))
			#if the threshold is reached, mark the pixel
	for x in range(1,width-1):
		for y in range(1,height-1):
			if int(tvals[width*y+x+4])>=hthreshold:
				fill(x,y,file2,tvals,theta,lthreshold);



	pixelsum=width*height
	return file2
if __name__ == "__main__":
	import sys
	ifilename="italy.ppm"
	#process command line arguments
	for opts in sys.argv:
		if opts == "--help" or opts== "-h":
			print "syntax: edgedetect [inputfile] [lower threshold] [higher threshold]"
			quit()
	if len(sys.argv)>1: #first argument is filename
		ifilename=sys.argv[1]
	if len(sys.argv)>2: #second argument is lthreshold
		lthreshold=int(sys.argv[2])
	if len(sys.argv)>3: #third argument is hthreshold
		hthreshold=int(sys.argv[3])
	strippedfilename=ifilename
	#take the extension off of the filename
	if ifilename[-4:]==".ppm" or ifilename[-4:]==".pgm":
		strippedfilename=ifilename[:-4]
	inlines=load(ifilename)
	#add suffix (so we make it clear what the file is)
	if inlines[0]=="P3":
		ofilename=strippedfilename+"-canny-"+str(lthreshold)+"-"+str(hthreshold)+".ppm"
	else:
		ofilename=strippedfilename+"-canny-"+str(lthreshold)+"-"+str(hthreshold)+".pgm"

	#create new image with edge pixels marked
	outarray=edgedetect(inlines)

	#write file
	print "DEBUG: writing to file "+ofilename
	outfile=open(ofilename,'w')
	for i in outarray:
		outfile.write(str(i)+"\n")
	outfile.close()
	print "%d/%d pixels detected as edges"%(pixelcount,pixelsum)

