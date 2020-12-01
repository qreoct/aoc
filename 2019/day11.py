#day11
import intcodecomputer
import copy
import os
import time

inputday11 = [3,8,1005,8,335,1106,0,11,0,0,0,104,1,104,0,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,102,1,8,28,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,101,0,8,51,1006,0,82,1006,0,56,1,1107,0,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,1001,8,0,83,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,101,0,8,104,1006,0,58,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,1001,8,0,129,1006,0,54,1006,0,50,1006,0,31,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,102,1,8,161,2,101,14,10,1006,0,43,1006,0,77,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,102,1,8,193,2,101,12,10,2,109,18,10,1,1009,13,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,226,1,1103,1,10,1,1007,16,10,1,3,4,10,1006,0,88,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,1001,8,0,263,1006,0,50,2,1108,17,10,1006,0,36,1,9,8,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,1002,8,1,300,1006,0,22,2,106,2,10,2,1001,19,10,1,3,1,10,101,1,9,9,1007,9,925,10,1005,10,15,99,109,657,104,0,104,1,21101,0,937268454156,1,21102,1,352,0,1106,0,456,21101,0,666538713748,1,21102,363,1,0,1105,1,456,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,3316845608,0,1,21102,1,410,0,1105,1,456,21101,0,209475103911,1,21101,421,0,0,1106,0,456,3,10,104,0,104,0,3,10,104,0,104,0,21101,0,984353603944,1,21101,444,0,0,1105,1,456,21102,1,988220752232,1,21102,1,455,0,1106,0,456,99,109,2,22101,0,-1,1,21102,40,1,2,21101,487,0,3,21101,0,477,0,1106,0,520,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,482,483,498,4,0,1001,482,1,482,108,4,482,10,1006,10,514,1102,0,1,482,109,-2,2105,1,0,0,109,4,2101,0,-1,519,1207,-3,0,10,1006,10,537,21101,0,0,-3,22101,0,-3,1,22101,0,-2,2,21102,1,1,3,21101,556,0,0,1106,0,561,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,584,2207,-4,-2,10,1006,10,584,21201,-4,0,-4,1106,0,652,22101,0,-4,1,21201,-3,-1,2,21202,-2,2,3,21101,0,603,0,1105,1,561,22101,0,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,622,21102,1,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,644,21201,-1,0,1,21101,644,0,0,105,1,519,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0]

hull = []
#make 8x8 hull
for i in range(200):
	mylist = []
	for ii in range(200):
		mylist.append('.')
	hull.append(mylist)

def showhull(hull, currx = None, curry = None):
	county=countx=0
	for i in hull:
		countx=0
		for ii in i:
			if county == int(curry) and countx == int(currx):
				print('@',end=" ")
			else: print(ii,end=" ")
			countx+=1
		county+=1
		print("",end="\n")

def changepiece(hull,x,y,newpiece):
	hull[y][x] = newpiece
	return hull

robot = intcodecomputer.IntComputer("Robot",copy.copy(inputday11),[],False)

halt = 1
currx = curry = 30
currdirection = 0 #compass[0] = 'n'
visited = {}

#changepiece(hull,currx,curry,'#')

while halt != -1:
	#showhull(hull,currx,curry)
	instruction = []
	compass = ['n','e','s','w']
	compassmoves = {
				'n': 'curry -= 1',
				's': 'curry += 1',
				'e': 'currx += 1',
				'w': 'currx -= 1'
				}
	robotface = {
				'n': '^',
				's': 'V',
				'e': '>',
				'w': '<'
				}

	#check the panel color that the robot is on
	if hull[curry][currx] == '.':
		print("x= {} y= {} panel is black".format(currx,curry))
		robotinput = [0]
	else:
		print("x= {} y= {} panel is white".format(currx,curry))
		robotinput = [1]
	robot.inputqueue = robotinput
	halt = robot.compute()
	instruction = robot.lastoutput
	print("My instructions are {}".format(instruction))
	#instruction[0] : 0 paint current black
	#				: 1 paint current white
	#instruction[1] : 0 turn left 90 deg
	#				: 1 turn right 90 deg
	#while instruction != []:
	if instruction[0]: changepiece(hull, currx, curry, '#')
	else: changepiece(hull, currx, curry, '.')

	if instruction[1]: 
		if currdirection == 3: currdirection = 0
		else: currdirection += 1
	else: 
		if currdirection == 0: currdirection = 3
		else: currdirection -= 1
	print("currdirection: {}".format(currdirection))
	#take a step forward
	print("Executing {}".format(compassmoves[compass[currdirection]]))
	exec(compassmoves[compass[currdirection]])
	print("robot Moved to x={} y={} {}".format(currx,curry,robotface[compass[currdirection]]))

	visited[(currx,curry)] = 1

		# if instruction != []:
		# 	instruction = instruction[2:]
		
	#time.sleep(10)
	robot.lastoutput.clear()
	#os.system('cls')



print(len(visited))