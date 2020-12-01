#true_list = [3,225,1,225,6,6,1100,1,238,225,104,0,1101,40,27,224,101,-67,224,224,4,224,1002,223,8,223,1001,224,2,224,1,224,223,223,1101,33,38,225,1102,84,60,225,1101,65,62,225,1002,36,13,224,1001,224,-494,224,4,224,1002,223,8,223,1001,224,3,224,1,223,224,223,1102,86,5,224,101,-430,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,1102,23,50,225,1001,44,10,224,101,-72,224,224,4,224,102,8,223,223,101,1,224,224,1,224,223,223,102,47,217,224,1001,224,-2303,224,4,224,102,8,223,223,101,2,224,224,1,223,224,223,1102,71,84,225,101,91,40,224,1001,224,-151,224,4,224,1002,223,8,223,1001,224,5,224,1,223,224,223,1101,87,91,225,1102,71,19,225,1,92,140,224,101,-134,224,224,4,224,1002,223,8,223,101,1,224,224,1,224,223,223,2,170,165,224,1001,224,-1653,224,4,224,1002,223,8,223,101,5,224,224,1,223,224,223,1101,49,32,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1107,226,677,224,1002,223,2,223,1006,224,329,101,1,223,223,8,226,226,224,1002,223,2,223,1005,224,344,101,1,223,223,1007,677,226,224,102,2,223,223,1005,224,359,101,1,223,223,8,226,677,224,102,2,223,223,1005,224,374,101,1,223,223,1107,677,677,224,1002,223,2,223,1005,224,389,1001,223,1,223,108,226,677,224,102,2,223,223,1005,224,404,1001,223,1,223,108,677,677,224,1002,223,2,223,1006,224,419,101,1,223,223,107,677,677,224,102,2,223,223,1006,224,434,101,1,223,223,108,226,226,224,1002,223,2,223,1006,224,449,1001,223,1,223,8,677,226,224,1002,223,2,223,1005,224,464,101,1,223,223,1108,226,677,224,1002,223,2,223,1006,224,479,1001,223,1,223,1108,677,677,224,1002,223,2,223,1005,224,494,101,1,223,223,7,677,677,224,1002,223,2,223,1005,224,509,101,1,223,223,1007,677,677,224,1002,223,2,223,1005,224,524,101,1,223,223,7,677,226,224,1002,223,2,223,1005,224,539,101,1,223,223,1107,677,226,224,102,2,223,223,1006,224,554,101,1,223,223,107,226,677,224,1002,223,2,223,1005,224,569,101,1,223,223,107,226,226,224,1002,223,2,223,1005,224,584,101,1,223,223,1108,677,226,224,102,2,223,223,1006,224,599,1001,223,1,223,1008,677,677,224,102,2,223,223,1006,224,614,101,1,223,223,7,226,677,224,102,2,223,223,1005,224,629,101,1,223,223,1008,226,677,224,1002,223,2,223,1006,224,644,101,1,223,223,1007,226,226,224,1002,223,2,223,1005,224,659,1001,223,1,223,1008,226,226,224,102,2,223,223,1006,224,674,1001,223,1,223,4,223,99,226]
true_list = [
3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99
]
import copy
from itertools import permutations

class intcomputer(object):
	def __init__(self,queue = []):
		self.list = copy.copy(true_list)
		self.opcode3_count = 0
		self.i = 0
		self.computeDone = False
		self.inputqueue = queue

	#   ABC DE
	#   010 01
	#   pip

	def getInstruction(self,instructions):
		if (instructions == 99):
			return 99
		else:
			return instructions


	def writeFunction(self,instructions):
		#purpose is to return a string to be exec(), with the correct operator (add/multiply)
		#and the correct position/immediate mode values

		operator = ''
		# if opcode 1
		if (str(instructions)[-1:] == '1'):
			operator = '+'
		# if opcode 2
		elif (str(instructions)[-1:] == '2'):
			operator = '*'

		# assume that parameter is set to position (i.e. the value of ABC is 000)
		a = 'self.list[self.list[i+3]]'
		b = 'self.list[self.list[i+1]]'
		c = 'self.list[self.list[i+2]]'

		# front 3 digits (if the opcode is <=99)
		if (instructions // 100 < 1):
			return (a + ' = ' + b + operator + c)
		# param 001 basically; 00101, 00102
		elif (999 >= instructions >= 100):
			if str(instructions)[0:1] == '1': b = 'self.list[i+1]'
			return (a + ' = ' + b + operator + c)
		# param 010, 011; 01001, 01002, 01101, 01102
		elif (9999 >= instructions >= 1000):
			if str(instructions)[1:2] == '1': b = 'self.list[i+1]'
			if str(instructions)[0:1] == '1': c = 'self.list[i+2]'
			return (a + ' = ' + b + operator + c)
		# param 111, 110, 101, 100; 11101, 11102, 11001, 11002, 10101, 10102, 10001, 10002
		elif (99999 >= instructions >= 10000):
			if str(instructions)[2:3] == '1': b = 'self.list[i+1]'
			if str(instructions)[1:2] == '1': c = 'self.list[i+2]'
			if str(instructions)[0:1] == '1': a = 'self.list[i+3]'
			return (a + ' = ' + b + operator + c)

	def opcode_fivesix(self,instructions, pos):
		#purpose is to return the first param and second param values
		#as a list, [firstparam, secondparam]
		firstparam = list[pos+1]
		secondparam = list[pos+2]
		
		
		# front 3 digits (if the opcode is <=99)
		if (instructions // 99 < 1):
			return [firstparam, secondparam]
		# param 001 basically; 0101, 00102
		elif (999 >= instructions >= 100):
			if str(instructions)[0:1] == '1': firstparam = pos+1
			return [firstparam, secondparam]
		# param 010, 011; 01001, 01002, 01101, 01102
		elif (9999 >= instructions >= 1000):
			if str(instructions)[1:2] == '1': firstparam = pos+1
			if str(instructions)[0:1] == '1': secondparam = pos+2
			return [firstparam, secondparam]

	def opcode_seveneight(self,instructions):
		#purpose is to return a string to be exec(), with the correct operator (lessthan/equals)
		#and the correct position/immediate mode values
		operator = ''
		# if opcode 7
		if (str(instructions)[-1:] == '7'):
			operator = '<'
		# if opcode 8
		elif (str(instructions)[-1:] == '8'):
			operator = '=='
		
		# assume that parameter is set to position (i.e. the value of ABC is 000)
		#1st param
		a = 'self.list[self.list[i+1]]'
		#2nd param
		b = 'self.list[self.list[i+2]]'
		#3rd param
		c = 'self.list[self.list[i+3]]'

		# front 3 digits (if the opcode is <=99)
		if (instructions // 100 < 1):
			#c = 1 if a == b else c = 0
			return (c + '= 1 if ' + a + operator + b + ' else 0')
		# param 001 basically; 00101, 00102
		elif (999 >= instructions >= 100):
			if str(instructions)[0:1] == '1': a = 'self.list[i+1]'
			return (c + '= 1 if ' + a + operator + b + ' else 0')
		# param 010, 011; 01001, 01002, 01101, 01102
		elif (9999 >= instructions >= 1000):
			if str(instructions)[1:2] == '1': a = 'self.list[i+1]'
			if str(instructions)[0:1] == '1': b = 'self.list[i+2]'
			return (c + '= 1 if ' + a + operator + b + ' else 0')
		# param 111, 110, 101, 100; 11101, 11102, 11001, 11002, 10101, 10102, 10001, 10002
		elif (99999 >= instructions >= 10000):
			if str(instructions)[2:3] == '1': c = 'self.list[i+3]'
			if str(instructions)[1:2] == '1': b = 'self.list[i+2]'
			if str(instructions)[0:1] == '1': a = 'self.list[i+1]'
			return (c + '= 1 if ' + a + operator + b + ' else 0')
		
	def compute(self):
		while self.computeDone == False:
			list = self.list
			todo = self.getInstruction(list[self.i])

			if str(todo)[-1:] == '1':
				# list[list[i+3]] = list[list[i+1]] + list[list[i+2]]
				exec(self.writeFunction(todo))
				self.i += 4
			elif str(todo)[-1:] == '2':
				# list[list[i+3]] = list[list[i+1]] * list[list[i+2]]
				exec(self.writeFunction(todo))
				self.i += 4
			elif str(todo)[-1] == '3':
				print("at i={}".format(self.i))
				print("Opcode 3 encountered! Waiting for input... Inputqueue is {}".format(self.inputqueue))
				if self.inputqueue == [] : break
				else:
					list[list[self.i + 1]] = self.inputqueue[0]
					self.i += 2
					self.inputqueue.pop()
			elif str(todo)[-1] == '4':
				if(todo // 100) == 1:
					print("Opcode 4 encountered! Output is {}".format(list[self.i+1]))
					return(list[self.i+1])
				else: 
					print("Opcode 4 encountered! Output is {}".format(list[list[self.i+1]]))
					return(list[list[self.i + 1]])
				self.i += 2
			elif str(todo)[-1] == '5':
				
				#if 1st param != 0:
				#   i= 2nd param
				#else:
				#   i+=2
				params = self.opcode_fivesix(todo,self.i)
				if list[params[0]] != 0:
					self.i = list[params[1]]
				else: 
					self.i+=3
				
			elif str(todo)[-1] == '6':
				params = self.opcode_fivesix(todo,self.i)
				if list[params[0]] == 0:
					self.i = list[params[1]]
				else: self.i+=3
			elif str(todo)[-1] == '7':
				exec(self.opcode_seveneight(todo))
				self.i += 4
			elif str(todo)[-1] == '8':
				print(todo)
				exec(self.opcode_seveneight(todo))
				self.i += 4

def phaseseq(a,b,c,d,e):
	return intcode(e, intcode(d, intcode(c, intcode(b, intcode(a,0)))))

l = list(permutations(range(5,10)))
print(l)

# for i in l:
# 	intcA = intcomputer([0,i[0]])
# 	intcB = intcomputer(i[1])
# 	intcC = intcomputer(i[2])
# 	intcD = intcomputer(i[3])
# 	intcE = intcomputer(i[4])
# 	intcA.compute()

intcA = intcomputer([18])
intcA.compute()