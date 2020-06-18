#Slam shuffle
import time
deck = []

def createdeck(size):
	deck = [x for x in range(size)]
	print("Deck created! {}".format(deck))
	return deck

def dealintonew(deck):
	deck.reverse()
	return deck

def cutN(instruction,deck):
	instruction = instruction.split(" ")
	N = int(instruction[1])
	if abs(N) > len(deck):
		print("N is too big! nothing happened")
		return deck
	tempdeck = []
	if N>0:
		for each in deck[N:len(deck)]:
			tempdeck.append(each)
		for each in deck[0:N]:
			tempdeck.append(each)
	if N<0:
		N = abs(N)
		for each in deck[-N:]:
			tempdeck.append(each)
		for each in deck[0:len(deck)-N]:
			tempdeck.append(each)
	return tempdeck

def dealwith(instruction,deck):
	instruction = instruction.split(" ")
	N = int(instruction[3])
	tempdeck = [x*0 for x in range(len(deck))]
	positions = generatepositions(N,len(deck))
	for each in positions:
		tempdeck[each] = deck[positions.index(each)]
	return tempdeck

def generatepositions(N,size):
	positions = []
	x = 0
	for i in range(size):
		positions.append(x)
		x+=N
		if x > size:
			x -= size
	return positions

def main(day22input):
	f = open(day22input).read().splitlines()
	deck = createdeck(119315717514047)
	time.sleep(2)
	for line in f:
		if line[0:3] == "cut":
			print("Instruction: {}".format(line))
			#cut function
			deck = cutN(line,deck)
			pass
		elif line[0:6] == "deal w":
			print("Instruction: {}".format(line))
			#deal with function
			deck = dealwith(line,deck)
			pass
		elif line[0:6] == "deal i":
			print("Instruction: {}".format(line))
			#deal into new function
			deck = dealintonew(deck)
		print("Result: {}...".format(deck[0:15]))
		print("Deck size: {}".format(len(deck)))
	print("Position of card 2019 is: {}".format(deck.index(2019)))
	return deck



if __name__ == "__main__":
	day22input = 'day22.txt'
	main(day22input)