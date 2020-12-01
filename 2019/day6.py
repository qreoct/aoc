f = open("day6.txt").read().splitlines()
mylist = ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L", "K)YOU", "I)SAN"]
planetdict = {}
import copy

class Node(object):
	def __init__(self, data):
		self.data = data
		self.child = []
		self.parent = []
	def __str__(self):
		return self.data
	def __repr__(self):
		return self.data
	def getName(self):
		return self.data
	def getChild(self):
		return self.child
	def getParent(self):
		return self.parent[0]
	def setChild(self, other):
		self.child.append(other)
		other.parent.append(self)
	def getPath(self, root, x, path):
		#recursive function that traverses all paths from root to find required node x
		#if node x is present then returns true and accumulates the paths in path[]
			if(root == None): return False
			if(root.data == x.data):
				return True
			else:
				if root.data == "COM" : path.append(root)
				for i in range(len(root.child)):
					path.append(root.child[i])
					if self.getPath(root.child[i], x, path):
						return True
					else:
						path.remove(root.child[i])
				return False


class Solution(object):
	def maxDepth(self, root):

		if not root:
			return 0

		if not root.child:
			return 1

		return 1 + max([self.maxDepth(node) for node in root.child])

	@staticmethod
	def findDist(root, node):
		#finds distance from root to desired node
		if (root == None):
			return -1
		dist = -1

		if(root.data == node.data):
			return dist + 1
		else:
			for i in range(len(root.child)):
				#print('checking node', root.child[i], ' against', node)
				dist = Solution.findDist( (root.child[i]), node)
				if dist >= 0:
					return dist + 1
		return dist


	@staticmethod
	def findLCA(n1,n2):
		n1path = []
		n2path = []
		n1.getPath(planetdict["COM"], n1, n1path)
		n2.getPath(planetdict["COM"], n2, n2path)
		n1path.reverse()
		n2path.reverse()
		for i in range(len(n1path)):
			for j in range(len(n2path)):
				if(n1path[i] == n2path[j]): return n1path[i]



for each in f:
	planet = each.split(')')
	if planet[0] in planetdict and planet[1] in planetdict:
		#print('both planets exist!')
		planetdict[planet[0]].setChild(planetdict[planet[1]])
	elif planet[0] in planetdict:
		#print('1 first planet exists. new planet' ,planet[1], ' created')
		planetdict[planet[1]] = Node(planet[1])
		planetdict[planet[0]].setChild(planetdict[planet[1]])
	elif planet[1] in planetdict:
		#print('2 second planet exists. new planet' ,planet[0], ' created')
		planetdict[planet[0]] = Node(planet[0])
		planetdict[planet[0]].setChild(planetdict[planet[1]])
	else:
		#print('- brand new planet' ,planet[0], planet[1], ' created')
		planetdict[planet[0]] = Node(planet[0])
		planetdict[planet[1]] = Node(planet[1])
		planetdict[planet[0]].setChild(planetdict[planet[1]])
		#print(planet[0], "has set a child of", planet[1])


#print(planetdict)
solve = Solution()
path1 = []
path2 = []
#findDist arguments are root,node
#getPath arguments are root,x


#finding the distance between two nodes on a Tree is given as
#dist(n1,n2) = dist(root,n1) + dist(root, n2) - 2*dist(root,lca)
#where lca is the Lowest Common Ancestor of n1 and n2 
#print(Solution.findDist(planetdict["YOU"] , planetdict["SAN"]))

#since we want to find distance between YOU and SANTA,

n1 = planetdict["YOU"].getParent()
n2 = planetdict["SAN"].getParent()

#dist = Solution.findDist(planetdict["COM"],n1) + Solution.findDist(planetdict["COM"],n2) - 2*Solution.findDist(planetdict["COM"],Solution.findLCA(n1,n2))
#print(dist)
print(planetdict["COM"].child)