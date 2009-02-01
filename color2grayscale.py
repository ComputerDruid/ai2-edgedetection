def color2grayscale(image):
	#first line=P3
	#second line=comment
	xyarray=file[2].split(" ")
	count=0
	outarray=[]
	temppixel=[]
	outarray.append("P2") #grayscale
	outarray.append("#written by an awesome (lame) ai class program")#comment
	outarray.append(file[2]) #dimensions
	outarray.append(file[3]) #depth

	for i in file[3:]:
		if count==3:
			count=0
			outarray.append(int(.3*temppixel[0]+.59*temppixel[1]+.11*temppixel[2]))
			temppixel=[]
		temppixel.append(int(i))
		count+=1
	return outarray

if __name__ == "__main__":
	file=open("italy.ppm").read().split("\n")[:-1]
	outarray=color2grayscale(file)
	for i in outarray:
		print i
