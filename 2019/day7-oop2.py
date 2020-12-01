#day7-oop 2
import intcodecomputer
import copy
from itertools import permutations

true_list = [
3,8,1001,8,10,8,105,1,0,0,21,42,51,76,101,118,199,280,361,442,99999,3,9,101,5,9,9,102,2,9,9,1001,9,4,9,102,2,9,9,4,9,99,3,9,1002,9,3,9,4,9,99,3,9,1002,9,4,9,1001,9,3,9,1002,9,5,9,101,3,9,9,1002,9,2,9,4,9,99,3,9,101,4,9,9,1002,9,2,9,1001,9,3,9,1002,9,3,9,101,4,9,9,4,9,99,3,9,101,3,9,9,1002,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99
]
ans = []
ansphase=[]
l = list(permutations(range(5,10)))
for i in l:

	intcA = intcodecomputer.IntComputer("A",copy.copy(true_list),[i[0],0],False)
	intcB = intcodecomputer.IntComputer("B",copy.copy(true_list),[i[1]],False)
	intcC = intcodecomputer.IntComputer("C",copy.copy(true_list),[i[2]],False)
	intcD = intcodecomputer.IntComputer("D",copy.copy(true_list),[i[3]],False)
	intcE = intcodecomputer.IntComputer("E",copy.copy(true_list),[i[4]],False)

	last = []
	intcA.compute()
	while intcA.lastoutput:
		intcB.inputqueue.append(intcA.lastoutput[0])
		intcA.lastoutput.pop()
		intcB.compute()
		while intcB.lastoutput:
			intcC.inputqueue.append(intcB.lastoutput[0])
			intcB.lastoutput.pop()
			intcC.compute()
			while intcC.lastoutput:
				intcD.inputqueue.append(intcC.lastoutput[0])
				intcC.lastoutput.pop()
				print(intcD.list)
				intcD.compute()
				while intcD.lastoutput:
					intcE.inputqueue.append(intcD.lastoutput[0])
					intcD.lastoutput.pop()
					intcE.compute()
					while intcE.lastoutput:
						intcA.inputqueue.append(intcE.lastoutput[0])
						last.append(intcE.lastoutput[0])
						intcE.lastoutput.pop()
						intcA.compute()
	ans.append(last.pop())
	ansphase.append(i)

print(max(ans))
print(ansphase[ans.index(max(ans))])

