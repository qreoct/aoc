#Day 3: Crossed Wires
from collections import defaultdict
class coord(object):
	def __init__(self, x, y):
		self.name = str("<{},{}>".format(x,y))
		self.x = x
		self.y = y
	def __str__(self):
		return self.name
	def __repr__(self):
		return self.name

class Line(object):
	def __init__(self,name,currX,currY):
		self.name = name
		self.currX = currX
		self.currY = currY
		self.coordList = [coord(currX,currY).name]
	def __str__(self):
		return self.name
	def __repr__(self):
		return self.name
	def getX(self):
		return self.currX
	def getY(self):
		return self.currY
	def getcoordList(self):
		return self.coordList
	def move(self, direction, steps):
		if(direction == "U"):
			x = 0
			y = 1
		elif(direction == "D"):
			x = 0
			y = -1
		elif(direction == "L"):
			x = -1
			y = 0
		elif(direction == "R"):
			x = 1
			y = 0
		for i in range(steps):
			self.currX += x
			self.currY += y
			coordgen = coord(self.currX, self.currY)
			self.coordList.append(coordgen.name)
		return None

def manhat(x,y):
	#returns manhattan distance from (x,y) to (0,0)
	return abs(x-0) + abs(y-0)
def removedupes(mylist):
	#remove duplicates from a list
	mylist = list ( dict.fromkeys(mylist) )
	return mylist
def indices(lst, element):
	#find all instances of an element in list and returns their index
    result = []
    offset = -1
    while True:
        try:
            offset = lst.index(element, offset+1)
        except ValueError:
            return result
        result.append(offset)


allcoords = defaultdict(int)

f = open("day3.txt").read().split("\n")
line1instruct = f[0].split(",")
line2instruct = f[1].split(",")

line1 = Line("line1",0,0)
line2 = Line("line2",0,0)

for i in line1instruct:
	direction = i[0:1]
	steps = int(i[1:])
	line1.move(direction,steps)
for i in line2instruct:
	direction = i[0:1]
	steps = int(i[1:])
	line2.move(direction,steps)

cleanline1 = removedupes(line1.coordList)
cleanline2 = removedupes(line2.coordList)
cleanlines = cleanline1+cleanline2

for each in cleanlines:
	allcoords[str(each)] +=1


#list of intersects
intersects = [key for key,value in allcoords.items() if allcoords[key]>1]
intersects.remove('<0,0>')
print("the intersects are {}".format(intersects))
bla = []
for i in intersects:
	i=i.strip('<>')
	bla.append(manhat(int(i.split(',')[0]), int(i.split(',')[1])))
print("min distance intersection is {}".format(min(bla)))

def stepstaken(coord,line):
	return indices(line.coordList,coord)

beststeps = []
for i in intersects:
	beststeps.append( stepstaken(i,line1)[0] + stepstaken(i,line2)[0] )
print(min(beststeps))
