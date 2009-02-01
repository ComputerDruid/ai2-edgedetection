file=open("italy.ppm").read().split("\n")[:-1]
#first line=P3
#second line=comment
xyarray=file[2].split(" ")
count=0
outarray=[]
temppixel=[]
for i in file[3:]:
	if count==3:
		count=0
		outarray.append(int(.3*temppixel[0]+.59*temppixel[1]+.11*temppixel[2]))
		temppixel=[]
	temppixel.append(int(i))
	count+=1
print "P2"
print "#written by an awesome (lame) ai class program"
print file[2]
print "255"
for i in outarray:
	print i
