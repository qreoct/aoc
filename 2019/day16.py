#Day 16: Flawed Frequency
#gdi

f = open("day16.txt").read()
signal = []
for char in f:
	signal.append(int(char))
# signal *= 10000

#getting search pos for part 2
# search = []
# for l in range(7):
# 	search.append(str(signal[l]))
# search = int("".join(search))
search = 0

def FFT(signal,phase):
	global i
	if(i == int(phase)):
		print("end")
		ans=[signal[k] for k in range(search,search+7)]
		print(ans)
		#return the search range
	else:
		i+=1
		print("---PHASE {}---".format(i))
		newlist = []
		for j in range(1,len(signal)+1):
			newlist.append(getDigit(signal,j))
			#print("---")
		#print("newlist is {}".format(newlist))
		FFT(newlist,phase)
		#run ftt on this input
		#then fft(newsignal,phase)
def getDigit(signal, position):
	#signal is a list of the whole thing, i.e. [1,2,3,4,5] for 12345
	half = len(signal)//2
	#getting Pattern Array (the 0, 1, 0, -1 thing):
	pattern = []
	if(position == len(signal)):return signal[-1]
	for i in range(position):
		pattern.append(0)
	for i in range(position):
		pattern.append(1)
	for i in range(position):
		pattern.append(0)
	for i in range(position):
		pattern.append(-1)
	length = len(pattern)
	patternpointer = position
	value = 0
	digit = position-1
	while digit < len(signal):
		if(patternpointer >= length): patternpointer = 0
		value += signal[digit]*pattern[patternpointer]
		#print("{} * {}".format(signal[digit],pattern[patternpointer]))
		#print("[{}]".format(value))
		patternpointer += 1
		digit += 1
	if abs(value) < 10:
		return abs(value)
	else: return abs(value)%10


i=0
FFT(signal,100)