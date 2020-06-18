class Moon(object):
	def __init__(self,name,x,y,z):
		self.name = name
		self.posx = int(x)
		self.posy = int(y)
		self.posz = int(z)
		self.velx = self.vely = self.velz = 0
	def getStatus(self):
		return("pos = <x={}, y={}, z={}>, vel = <x={}, y={}, z={}>".format(self.posx, self.posy, self.posz, self.velx, self.vely, self.velz))


moondict = {}
count = 0
import itertools
import timeit
from collections import defaultdict

#opening input and creating moons
f = open('day12.txt').read().splitlines()
for i in f:
	i = i.strip('<>')
	j = i.split(',')
	x = int(j[0].replace("x=",""))
	y = int(j[1].replace("y=",""))
	z = int(j[2].replace("z=",""))
	moondict[count] = Moon(count,x,y,z)
	count += 1

def showmoons():
	for i in moondict:
		print (moondict[i].getStatus())

#get a tuple list containing all pairs of moons
moonpairs = list(itertools.combinations(range(len(moondict)),2))
starttime = 0
seenstates = defaultdict(lambda: (0,0))
def start(timestep):
	starttime = timeit.default_timer()
	#case where timestep is defined (part 1)
	initx = inity = initz = (0,0,0,0)
	first_1 = first_2 = first_3 = True
	if int(timestep) > 0:
		for i in range(int(timestep)+1):
			#first step do nothing
			if i == 0: pass
			else:
				for pair in moonpairs:
					#run gravity on each moonpair (i.e. change their velocity)
					gravity(pair[0],pair[1])
				for moon in moondict:
					velocity(moondict[moon])
				#if(seenstates[getstate(moondict)][0] == 1):
					#1st time seeing dupe, which means you can get the LENGTH of chain
					#print("saw first instance dupe!")
				#	previ = seenstates[getstate(moondict)][1]
				#	seenstates[getstate(moondict)] = (2, i-previ)
				#elif(seenstates[getstate(moondict)][0] == 2):
					#SEEN dupe before! skip i steps
				#	print("saw second instance dupe!")
				#	i += seenstates[getstate(moondict)][1]
				#else:seenstates[getstate(moondict)] = (1, i)
				if(getvel('x',moondict) == initx) : 
					if(first_1 == True):
						print("first vel dupe for x at i=",i)
						first_1 = False
				if(getvel('y',moondict) == inity) : 
					if(first_2 == True):
						print("first vel dupe for y at i=",i)
						first_2 = False
				if(getvel('z',moondict) == initz) : 
					if(first_3 == True):
						print("first vel dupe for z at i=",i)
						first_3 = False
	#case where you want to run infinitely (part 2)
	#TODO remember to fix all calls to getstate!
	else:
		found = False
		i = 0
		initstate = getstate(moondict)
		print("initstate is",initstate)
		while found == False:
			for pair in moonpairs:
				#run gravity on each moonpair (i.e. change their velocity)
				gravity(pair[0],pair[1])
			for moon in moondict:
				velocity(moondict[moon])
			if i==0: 
				print("first run")
			else:
				if(getvel('x',moondict) == initx) : 
					if(first_1 == True):
						print("first vel dupe for x at i=",i+1)
						first_1 = False
				if(getvel('y',moondict) == inity) : 
					if(first_2 == True):
						print("first vel dupe for y at i=",i+1)
						first_2 = False
				if(getvel('z',moondict) == initz) : 
					if(first_3 == True):
						print("first vel dupe for z at i=",i+1)
						first_3 = False
				if (first_1 == False and first_2 == False and first_3 == False): found = True
			i += 1
		return True

def gravity(a,b):
	moon1 = moondict[a]
	moon2 = moondict[b]
	if moon1.posx < moon2.posx:
		moon1.velx += 1
		moon2.velx -= 1
	elif moon1.posx > moon2.posx:
		moon1.velx -= 1
		moon2.velx += 1
	else: pass
	if moon1.posy < moon2.posy:
		moon1.vely += 1
		moon2.vely -= 1
	elif moon1.posy > moon2.posy:
		moon1.vely -= 1
		moon2.vely += 1
	else: pass
	if moon1.posz < moon2.posz:
		moon1.velz += 1
		moon2.velz -= 1
	elif moon1.posz > moon2.posz:
		moon1.velz -= 1
		moon2.velz += 1
	else: pass
def velocity(moon):
	moon.posx += moon.velx
	moon.posy += moon.vely
	moon.posz += moon.velz
def getenergy(system):
	totale = 0
	for each in system:
		totale += getpe(each) * getke(each)
	return totale
def getpe(moon):
	return abs(moondict[moon].posx) + abs(moondict[moon].posy) + abs(moondict[moon].posz)
def getke(moon):
	return abs(moondict[moon].velx) + abs(moondict[moon].vely) + abs(moondict[moon].velz)
def getstate(system):
	#returns list of tuple of current state of system in the form of (moon1.posx, moon1.posy, moon1.posz, moon1.velx ...)
	allmoons = []
	for moon in system:
		templist = []
		templist.append(moondict[moon].posx)
		templist.append(moondict[moon].posy)
		templist.append(moondict[moon].posz)
		templist.append(moondict[moon].velx)
		templist.append(moondict[moon].vely)
		templist.append(moondict[moon].velz)
		allmoons.append(tuple(templist))
	return allmoons
def getmoonstate(moon):
	#return tuple of current state of moon (posx,posy,posz,velx,vely,velz)
	templist = []
	templist.append(moondict[moon].posx)
	templist.append(moondict[moon].posy)
	templist.append(moondict[moon].posz)
	templist.append(moondict[moon].velx)
	templist.append(moondict[moon].vely)
	templist.append(moondict[moon].velz)
	return tuple(templist)
def getvel(axis,system):
	if str(axis) =="x":
		toople = [moondict[moon].velx for moon in system]
		return( tuple(toople) )
	elif str(axis) =="y":
		a,b,c,d = [moondict[moon].vely for moon in system]
		return(a,b,c,d)
	elif str(axis) =="z":
		a,b,c,d = [moondict[moon].velz for moon in system]
		return(a,b,c,d)



start(input("how many cycles?"))
stop = timeit.default_timer()
print("time taken", stop-starttime, "s")