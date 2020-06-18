#Day 10
#Monitoring Station
import math
import time
from collections import defaultdict
f = open("day10.txt").read().splitlines()

#coordinate list of asteroids in tuple form
roidlist = []
anglelist = defaultdict(list)
x=0
y=0
for line in f:
	for char in line:
		if str(char) == ".": pass #empty
		else: #it's a roid
			roidlist.append( (x,y) )
		x+=1
	x=0
	y+=1

#some functions
#get angle from roid (return angle A from roid # looking at @ relative to the X plane)
#check visible (check if angle A already exists in visible roids)

def getAngle(roidA,roidB):
	#roidA[0] = x
	#roidA[1] = y
	return math.degrees(math.atan2(roidA[1]-roidB[1], roidA[0]-roidB[0]))

def getVisiblesAngles(roid,getAngles):
	#function to return number of visible asteroids

	#list of asteroids (tuple) that roid has seen
	visiblelist = []
	#list of angles that roid has seen
	if getAngles == True: 
		global anglelist
		anglelist.clear()
	else: 
		anglelist = defaultdict(list)
	#list of all asteroids
	global roidlist
	for asteroid in roidlist:
		if(asteroid == roid):pass
		else: 
			if getAngle(roid,asteroid) not in anglelist:
				#print("i see roid {} at angle {}".format(asteroid,getAngle(roid,asteroid)))
				anglelist[getAngle(roid,asteroid)].append(asteroid)
				visiblelist.append(asteroid)
			else: 
				anglelist[getAngle(roid,asteroid)].append(asteroid)
	#print("{} can see {} other roids".format(roid,len(visiblelist)))
	if getAngles == True: return anglelist
	else: return len(visiblelist)

def distance(roidA, roidB):
	#returns float distance from A to B
	return math.sqrt( (roidB[0]-roidA[0])**2 + (roidB[1]-roidA[1])**2 )

def shootAngle(angle):
	global anglelist, monitoringstation, asteroids_destroyed
	#if no roids left at that angle, delete that angle
	if(anglelist[angle] == []):
		print("angle of {} empty. deleting!".format(anglelist[angle]))
		del anglelist[angle]
	else:
		distlist=[]
		for asteroid in anglelist[angle]:
			#print("asteroid:{}, monitoringstation:{}".format(asteroid,monitoringstation))
			distlist.append(float(distance(asteroid,monitoringstation)))
		#closest asteroid: anglelist[angle][distlist.index(min(distlist))]
		#print("{} deleted!".format(anglelist[angle][distlist.index(min(distlist))]))

		changemap(anglelist[angle][distlist.index(min(distlist))] , "*")
		asteroids_destroyed += 1
		del anglelist[angle][distlist.index(min(distlist))]
	return None


def part1():
	anslist = dict()
	for each in roidlist:
		anslist[each] = getVisiblesAngles(each,False)
	#print(anslist)
	#print ("Roid {} can see {} other roids".format(max(anslist, key=anslist.get), anslist[max(anslist, key=anslist.get)]))


monitoringstation = (19,14)
#for actual input it's 19,14
asteroids_destroyed = 0
def part2():
	global monitoringstation
	print("Monitoring Station is at {}".format(monitoringstation))
	anglelist = getVisiblesAngles(monitoringstation,True)
	s = sorted(anglelist)
	i = s.index(90.0)
	while asteroids_destroyed<200:
		#print("Shooting at angle {}".format(s[i]))

		printmap(newf)
		time.sleep(0.2)
		shootAngle(s[i])
		i+=1
		if i>=len(s):i=0

def printmap(f):
	for line in f:
		for char in line:
			print("{}".format(char),end="")
		print("\n", end="")

def changemap(xy,char):
	global newf
	x = xy[0]
	y = xy[1]
	newchar = str(char)
	newf[y][x] = newchar

newf = []
for line in f:
	row = []
	for char in line:
		if(char == "."): row.append(" ")
		else:row.append(str(char))
	newf.append(row)

#printmap(newf)

#change monitoring station to spaceship

changemap(monitoringstation,'A')
part1()
part2()
