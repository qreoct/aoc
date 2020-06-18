f = open('day8.txt').read().splitlines()

from collections import defaultdict

#dictionary that stores no. of 0, 1 and 2s.
#key = layer number
#e.g. layer 5 has 18 2s:
#5 : 18

# my pic has 150 pixels in total, this dict stores the color at each pixel
pic = defaultdict(lambda:2)

def getPic (width,height,data):
	layercount = 1
	pixelnum = 1
	while len(data) > 0:
		for h in range(height):
			foo = data[0:width]
			for w in range(width):
				#if it's transparent, then save the new number
				if (int(pic[pixelnum]) == 2):
					pic[pixelnum] = foo[w]
				pixelnum += 1
			data = data[width:]
		pixelnum = 1
		layercount += 1

def printPic (width,height,data):
	pixelnum = 1
	line=''
	for h in range(height):
		for w in range(width):
			if data[pixelnum] == '0': line += ' '
			elif data[pixelnum] == '1': line += '0'
			elif data[pixelnum] == '2': line += ' '
			pixelnum += 1
		print(line)
		line = ''
getPic(25,6, f[0])
printPic(25,6,pic)

