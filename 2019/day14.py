#Day 14
#Space Stoichiometry

from collections import defaultdict
import math

class Graph(object):
	def __init__(self, name):
		self.name = name
		self.vertices = defaultdict() #a list of nodes
		self.edges = [] #a list of edges in tuple form (u,v, weight)
	def __str__(self):
		#return str(self.name + str(self.vertices) + str(self.edges))
		return "Graph Name: {} \nGraph Vertices: {} \nGraph Edges: {}".format(self.name, str(self.vertices), str(self.edges))
	def __repr__(self):
		return self.name
	def setNode(self, name):
		self.vertices[name] = Node(name)
	def setEdge(self, u, v, weight):
		data = (self.vertices[u],self.vertices[v],weight)
		self.vertices[u].edges.append( data )
		self.vertices[v].edges.append( data )
		self.edges.append( data )

class Node(object):
	def __init__(self, name, value = 1):
		self.name = name
		self.value = value
		self.edges = []
	def __str__(self):
		return self.name
	def __repr__(self):
		#return str(str(self.value) + self.name)
		#as of now don't return value
		return self.name
	def setValue(self, newval):
		self.value = newval
	def getEdge(self):
		return self.edges

def getOres(chemical, wanted_amt, wastedList, resultsList):
	smallest_amt = stoichio.vertices[chemical].value
	if chemical not in wastedList:
		wastedList[chemical] = 0

	while wastedList[chemical] >= 1:
		wanted_amt -=1
		wastedList[chemical] -=1

	reaction_repeats = math.ceil(wanted_amt/smallest_amt)
	reaction_result_amt = smallest_amt * reaction_repeats

	if wanted_amt == 0:
		print("end reaction")
		return

	wasted_mat = reaction_result_amt - wanted_amt
	wastedList[chemical] += wasted_mat

	children = []
	for i in stoichio.vertices[str(chemical)].getEdge():
		if (str(i[1])==str(chemical)):
			children.append(i)
	for i in children:
		children_needed = int(i[2][0])  * reaction_repeats
		#print("child now is {}".format(i))
		if (str(i[0]) == "ORE"):
			resultsList["ORE"] += children_needed
		else:
			getOres(str(i[0]), children_needed, wastedList, resultsList)
	#print("wastedlist is {}".format(wastedList))
	return resultsList


stoichio = Graph("chio")

f = open("day14.txt").read().splitlines()
rightside=[]

for line in f:
	rightside.append(line.split(" => ")[1].split(","))
for each in rightside:
	each = str(each[0]).split(" ")
	stoichio.setNode(str(each[1]))
	stoichio.vertices[str(each[1])].setValue(int(each[0]))
print(stoichio.vertices)

for line in f:
	equation = line.split(" => ")
	#equation[0] is left side
	#equation[1] is right side
	leftside = equation[0].split(",")
	rightside = equation[1].split(",")
	leftnodes = []
	rightnodes = []
	for each in leftside:
		each = each.strip(" ")
		each = each.split(" ")
		if(str(each[1]) in stoichio.vertices):
			pass
		else:
			print("LEFT: creating Node called {}".format(str(each[1])))
			stoichio.setNode(str(each[1]))
		leftnodes.append( (int(each[0]), str(each[1])) )
	for each in rightside:
		each = each.strip(" ")
		each = each.split(" ")
		rightnodes.append( (int(each[0]), str(each[1])) )
	for left in leftnodes:
		for right in rightnodes:
			stoichio.setEdge(left[1], right[1], ( left[0],right[0]) )
			#stoichio.setEdge(left[1], right[1], math.ceil(left[0]/stoichio.vertices[left[1]].value) )
			#what if i didn't set the last arg of edge as a tuple?

	print("--- line {} ---".format(line))


print(stoichio)

# part 1, getOres
# wastedList = dict()
# resultsList = {"ORE":0}
# print(getOres("FUEL",1,wastedList,resultsList))

#part 2, getFuel
# approx = 1000000000000//97422
# wastedList = dict()
# resultsList = {"ORE":0}
# fueltally=0
# fueltally += approx
# print(getOres("FUEL",13108426,wastedList,resultsList))
#remaining ores : 1tril - 783055187769
#				: 216944812231
maxfuel = 10264621
wastedList = dict()
resultsList = {"ORE":0}
oresUsed = 0
remainingOres = 1000000000000
while oresUsed <= 1000000000000:
	getOres("FUEL",maxfuel,wastedList,resultsList)
	oresUsed += resultsList['ORE']
	remainingOres -= resultsList['ORE']
	print("remainingores: {}".format(remainingOres))
	print(remainingOres//97422)
	maxfuel += (remainingOres//97422)
	resultsList["ORE"] = 0
	print("maxfue is {}".format(maxfuel))
print(maxfuel)
