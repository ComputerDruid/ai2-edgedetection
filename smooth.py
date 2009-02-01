thisAlgorithmBecomingSkynetCost=999999999

file=open("italy.pgm").read().split("\n")[:-1]
file2=file[:]
#first line=P2
#second line=comment
def getpixel(x,y):
	return int(file[y*width+x+4])
xyarray=file[2].split(" ")
width=int(xyarray[0])
height=int(xyarray[1])
count=0
for x in range(1,width-1):
	for y in range(1,height-1):
		file2[width*y+x+4]=int((1*getpixel(x-1,y-1)+2*getpixel(x,y-1)+1*getpixel(x+1,y-1)+2*getpixel(x-1,y)+4*getpixel(x,y)+2*getpixel(x+1,y)+1*getpixel(x-1,y+1)+2*getpixel(x,y+1)+1*getpixel(x+1,y+1))/16)
for i in file2:
	print i
