#Intcode computer
import copy
class IntComputer(object):
	def __init__(self,name,code,inputqueue = None,debug=False,relativebase=0):
		self.i = 0
		#instruction pointer
		self.name = name
		self.list = code
		self.resetlist = copy.copy(code)
		self.inputqueue = inputqueue
		self.debug = debug
		self.lastoutput = []
		self.relativebase = relativebase
		self.memory = []
		self.list = self.expandList(self.list)


	def reset(self):
		self.list = copy.copy(self.resetlist)

	def expandList(self,list):
		"""
		day 9 wants you to expand the memory by a lot
		"""
		for i in range(10000-len(list)):
			list.append(0)
		return list

	def getInstruction(self,instructions):
		if (instructions == 99):
			return 99
		else:
			return instructions

	def getMode(self,instructions):
		"""
		Converts mode to 5 digit list
		e.g. 101 to [0,0,1,0,1]
		"""
		converted=[]
		for char in str(instructions):
			converted.append(int(char))
		for i in range(5-len(converted)):
			converted.insert(0,0)
		return converted

	def opcodeOneTwo(self,inputs):
		i = self.i
		param1MODE = inputs[2]
		param2MODE = inputs[1]
		param3MODE = inputs[0]
		if param1MODE == 1: param1 = self.list[i+1]
		elif param1MODE == 2: param1 = self.list[self.relativebase + self.list[i+1]] 
		else: param1 = self.list[self.list[i+1]]
		if param2MODE == 1: param2 = self.list[i+2]
		elif param2MODE == 2: param2 = self.list[self.relativebase + self.list[i+2]] 
		else: param2 = self.list[self.list[i+2]]
		if param3MODE == 1: param3 = self.list[i+3]
		elif param3MODE == 2: param3 = self.relativebase + self.list[i+3]
		else: param3 = self.list[self.list[i+3]]
		if inputs[4] == 1:
			#add
			if self.debug: print("{}\n{} + {} saved at {}".format(self.list[i:i+4],param1,param2,param3))
			if param3MODE == 1:
				self.list[i+3] = param1+param2
			elif param3MODE == 2:
				self.list[param3] = param1+param2
			else: 
				self.list[self.list[i+3]] = param1+param2
		elif inputs[4] == 2:
			#multiply
			if self.debug: print("[{}]\n{} * {} saved at {}".format(self.list[i:i+4],param1,param2,param3))
			if param3MODE == 1: 
				self.list[i+3] = param1*param2
			elif param3MODE == 2:
				self.list[param3] = param1*param2
			else: 
				self.list[self.list[i+3]] = param1*param2

	def opcodeFiveNine(self,inputs):
		i = self.i
		param1MODE = inputs[2]
		param2MODE = inputs[1]
		param3MODE = inputs[0]
		if param1MODE == 1: param1 = self.list[i+1]
		elif param1MODE == 2: param1 = self.list[self.relativebase + self.list[i+1]] 
		else: param1 = self.list[self.list[i+1]]
		if param2MODE == 1: param2 = self.list[i+2]
		elif param2MODE == 2: param2 = self.list[self.relativebase + self.list[i+2]] 
		else: param2 = self.list[self.list[i+2]]
		#only set param 3 for opcode 5,6
		if inputs[4] >= 7:
			if param3MODE == 1: param3 = i+3
			elif param3MODE == 2: param3 = self.relativebase + self.list[i+3]
			else: param3 = self.list[i+3]
			if self.debug:print("param3 is {}".format(param3))
		if inputs[4] == 5:
			if self.debug: print("Jump if true {}".format(param1))
			#jump if true
			if self.debug: print("Jump target {}".format(param2))
			if param1: 
				if self.debug: print("Jumped")
				self.i=param2
			else: self.i+=3
		if inputs[4] == 6:
			if self.debug: print("Jump if false {}".format(param1))
			#jump if false
			if self.debug: print("Jumping to {}".format(param2))
			if not param1:
				if self.debug: print("Jumped")
				self.i=param2
			else: self.i+=3
		if inputs[4] == 7:
			#lessthan
			if self.debug: print("Check {} < {}".format(param1,param2))
			if param1 < param2: 
				if self.debug: print("true! wrote 1 at pos{}".format(param3))
				self.list[param3] = 1
				if self.debug: print("verified written: {}".format(self.list[param3]))
			else: self.list[param3] = 0
			self.i +=4
		if inputs[4] == 8:
			if self.debug: print("Check {} = {}".format(param1,param2))
			if param1 == param2: 
				if self.debug: print("true! wrote 1 at pos{}".format(param3))
				self.list[param3] = 1
				if self.debug: print("verified written: {}".format(self.list[i + 3]))
			else: 
				if self.debug: print("saved 0 at list[{}]".format(param3))
				self.list[param3] = 0
			self.i += 4


	def compute(self):
		if self.debug: print("Computer {} with inputqueue {} lastoutput {} and relativebase {}".format(self.name,self.inputqueue,self.lastoutput, self.relativebase))
		while True:
			todo = self.getInstruction(self.list[self.i])
			#print("list[0] is {}".format(self.list[0]))
			if str(todo)[-2:] == '99':
				#print(self.name + " halting!")
				return -1
				break
			if str(todo)[-1:] == '1' or str(todo)[-1:] == '2':
				if self.debug: print("i={} opcode={} doing OneTwo...".format(self.i,todo))
				self.opcodeOneTwo(self.getMode(todo))
				self.i+=4
			if str(todo)[-1:] == '3':
				#print("Input taken {}".format(self.inputqueue))
				if self.debug: print("i={} opcode={} getting input of {}".format(self.i,todo,self.inputqueue))
				if self.inputqueue==[]:
					print(self.name + " waiting for input...")
					return -2
					break
				if self.getMode(todo)[2] == 2: #Relative mode
				# 203,5, relative base = 6
				# "Take input and save in list[5+6]"
					if self.debug: print("Input of {} saved at list[{}+{}]".format(self.inputqueue[0],self.relativebase,self.list[self.i+1]))
					self.list[self.relativebase + self.list[self.i+1]] = self.inputqueue[0]
				else: #Immediate mode
					self.list[self.list[self.i+1]] = self.inputqueue[0]
				del self.inputqueue[0]
				self.i+=2
			if str(todo)[-1:] == '4':
				if self.debug: print("i={} opcode={}".format(self.i,todo))
				if self.getMode(todo)[2] == 1: #Immediate mode
					if self.debug: print(self.name + " OUTPUT: {}".format(self.list[self.i+1]))
					#self.lastoutput.clear()
					self.lastoutput.append(self.list[self.i+1])
				elif self.getMode(todo)[2] == 2: #Relative mode
					if self.debug: print("relbase {}".format(self.relativebase))
					if self.debug: print(self.name + " OUTPUT: {}".format(self.list[self.relativebase + self.list[self.i+1]]))
					#self.lastoutput.clear()
					self.lastoutput.append(self.list[self.relativebase + self.list[self.i+1]])
				else: #Position mode
					if self.debug: print(self.name + " OUTPUT: {}".format(self.list[self.list[self.i+1]]))
					#self.lastoutput.clear()
					self.lastoutput.append(self.list[self.list[self.i+1]])
				self.i+=2
			if str(todo)[-1:] == '5' or str(todo)[-1:] == '6' or str(todo)[-1:] == '7' or str(todo)[-1:] == '8':

				if self.debug: print("At {} for i={}".format(self.list[self.i:self.i+4],self.i))
				self.opcodeFiveNine(self.getMode(todo))
			if str(todo)[-1:] == '9':
				if self.debug: print("At {} for i={}".format(self.list[self.i:self.i+2],self.i))
				if self.getMode(todo)[2] == 2: #Relative mode
					if self.debug: print("checking pos {}".format(self.relativebase + self.list[self.i+1]))
					if self.debug: print("value is {}".format(self.list[self.relativebase + self.list[self.i+1]]))
					if self.debug: print("Relative base is {} + {}".format(self.relativebase,self.list[self.relativebase + self.list[self.i+1]]))
					self.relativebase += self.list[self.relativebase + self.list[self.i+1]]
				elif self.getMode(todo)[2] == 1: #Position mode
					if self.debug: print("Relative base is {} + {}".format(self.relativebase,self.list[self.i+1]))
					self.relativebase += self.list[self.i+1]
				else:
					if self.debug: print("Relative base is {} + {}".format(self.relativebase,self.list[self.list[self.i+1]]))
					self.relativebase += self.list[self.list[self.i+1]]
				self.i+=2