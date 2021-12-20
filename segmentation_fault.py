import os 

def ReadData():
	output = []
	with open(os.getcwd() + '/data/segmentation_fault_test.txt') as file:
		count = 1
		for line in file:
			raw_data = line.split(" | ")
			output_data = raw_data[1]
			output_data = output_data.strip("\n")
			output.append(output_data.split(" "))
	return output

ONE = 2
FOUR = 4
SEVEN = 3
EIGHT = 7
checks = [ONE, FOUR, SEVEN, EIGHT]

def SimpleSegmentation():
	data = ReadData()
	print(str(data))

	counts = []
	for data_set in data:
		for entry in data_set:
			length = len(entry)
			while length + 1 > len(counts):
				counts.append(0)
			counts[length] += 1

	total = 0
	for check in checks:
		total += counts[check]

	print(total)

def IsRearrangement(word1, word2):
	if len(word1) != len(word2):
		return False
	world1split = sorted(word1)
	world2split = sorted(word2)
	i = 0
	while i < len(word1):
		if world1split[i] != world2split[i]:
			return False	
		i += 1
	return True

def IsSubstring(string, substring):
	for subl in substring:
		found = False
		for l in string:
			if l == subl:
				found = True
		if not found:
			return False
	return True

def DecipherEnigma(enigma, output):
	for entry in enigma:
		if len(entry) == 2:
			output[1] = entry
		elif len(entry) == 3:
			output[7] = entry
		elif len(entry) == 4:
			output[4] = entry
		elif len(entry) == 7:
			output[8] = entry

	for entry in enigma:
		if len(entry) == 6:
			if IsSubstring(entry, output[4]):
				output[9] = entry
			elif IsSubstring(entry, output[1]):
				output[0] = entry
			else:
				output[6] = entry
		elif len(entry) == 5:
			if IsSubstring(entry, output[7]):
				output[3] = entry
			elif output[6] != 0:
				if IsSubstring(output[6], entry):
					output[5] = entry
				else:
					output[2] = entry
	
	rerun = False
	for entry in output:
		if entry == 0:
			rerun = True
	if rerun:
		DecipherEnigma(enigma, output)

	return output
			
def ProcessEntry(entry):
	enigma = entry[0].split(" ")
	data = entry[1].split(" ")

	output = [0,0,0,0,0,0,0,0,0,0]
	codex = DecipherEnigma(enigma, output)

	result = ""
	for word in data:
		index = 0
		for code in codex:
			if IsRearrangement(word, code):
				result += str(index)
			index += 1

	return int(result)

def ComplexReadData():
	output = []
	with open(os.getcwd() + '/data/segmentation_fault.txt') as file:
		for line in file:
			line = line.strip("\n")
			raw_data = line.split(" | ")
			output.append(raw_data)
	return output		
			

def ComplexSegmentation():
	data = ComplexReadData()

	totals = []
	for entry in data:
		totals.append(ProcessEntry(entry))

	result = 0
	for total in totals:
		result += int(total)
	print(result)

	
ComplexSegmentation()




