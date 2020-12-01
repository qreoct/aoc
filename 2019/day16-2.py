#Day 16: Flawed Frequency
#gdi

#the pattern is: only the last n digits will affect themselves
#i.e. if you want to find the last n digits of input length m
#just delete the rest and only run the FFT on the last n digits
#thus e.g. if m=320000, n=303673, just focus on last m-n digits

f = open("day16.txt").read()
signal = []
for char in f:
	signal.append(int(char))
signal *= 10000

#getting search pos for part 2
search = []
for l in range(7):
	search.append(str(signal[l]))
search = int("".join(search))
#search = 0

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
	#getting Pattern Array (the 0, 1, 0, -1 thing):
	pattern = []
	#if position <= half: return 0
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
#FFT(signal,100)


#new FFT:
#FFT(signal, n, phase)
#chops signal to become the last n digits
def chopsignal(signal, n):
	signal = signal[n:len(signal)+1]
	return signal

def neogetNewlist(cumsum, signal):
	newlist = []
	#print("cumsum first time: {}".format(cumsum))
	for digit in signal:
		lastdigit = cumsum%10
		newlist.append(lastdigit)
		cumsum -= int(digit)
	return newlist

def getcumSum(signal):
	#print("getting cumsum of {} digits".format(len(signal)))
	sum = 0
	for digit in signal:
		sum += int(digit)
	return sum

def neoFFT(signal, phase):
	global i
	if(i == int(phase)):
		print("end")
		ans=[signal[k] for k in range(8)]
		print(ans)
	else:
		i+=1
		print("---PHASE {}---".format(i))
		newlist = []
		cumsum = getcumSum(signal)
		newlist = neogetNewlist(cumsum,signal)
		#print("newlist is {}".format(newlist))
		neoFFT(newlist,phase)

signal = chopsignal(signal,search)
print("chopped signal length is {}".format(len(signal)))
#signal = chopsignal(signal,3)
#print("newsignal is {}".format(signal))
neoFFT(signal,100)
print("search string was {}".format(search))
#neoFFT([5,6,7,8],4)