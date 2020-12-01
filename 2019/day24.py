#day24
import time
import copy
f = open('day24.txt').read().splitlines()

bugs = []
for line in f:
	mylist=[]
	for char in line:
		mylist.append(char)
	bugs.append(mylist)

newlist = copy.copy(bugs)

def updatestate(bugs):
	x=y=0
	for line in bugs:
		x=0
		for bug in line:
			checkstate(bug,x,y,newlist)
			x+=1
		y+=1
	bugs.clear()
	bugs = copy.copy(newlist)
	return bugs

def checkstate(nowchar,x,y,newlist):
	if nowchar == "#":
		#print("checking x{} y{} is {} neighbours {}".format(x,y,nowchar,getneighbours(x,y,bugs)))

		if getneighbours(x,y,bugs) == 1:
			newlist[y][x] = "."
	elif nowchar == ".":
		#print("checking x{} y{} is {} neighbours {}".format(x,y,nowchar,getneighbours(x,y,bugs)))
		if getneighbours(x,y,bugs) == 1 or getneighbours(x,y,bugs) == 2:
			newlist[y][x] = "#"

def getneighbours(x,y,bugs):
	score = 0
	try:
		if bugs[x+1][y] == "#": score+=1
		if bugs[x-1][y] == "#": score+=1
		if bugs[x][y+1] == "#": score+=1
		if bugs[x][y-1] == "#": score+=1
		print("up{} down{} right{} left{}".format(bugs[y+1][x],bugs[y-1][x],bugs[y][x+1],bugs[y][x-1]))
	except:
		pass
	return score

def showbugs(bugs):
	for line in bugs:
		for i in line:
			print(i,end="")
		print("",end="\n")

print("Bugs are:")
showbugs(bugs)

print("state has been updated")
bugs = updatestate(bugs)

print("Bugs are:")
showbugs(bugs)