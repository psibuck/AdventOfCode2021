import os 

def ReadData():
	data = []
	with open(os.getcwd() + '/data/syntax_sorting.txt') as file:
		for line in file:
			line = line.strip("\n")
			data.append(line)
	return data

OpeningBrackets = ["(", "[", "{", "<"]
ClosingBrackets = [")", "]", "}", ">"]
Scores = [3, 57, 1197, 25137]

def GetIndex(array, value):
	index = -1
	while index < len(array) - 1:
		index += 1
		if array[index] == value:
			return index
	return -1

def ProcessChunk(chunk):
	opening_brackets = []
	for c in chunk:
		index = GetIndex(OpeningBrackets, c)
		if index != -1:
			opening_brackets.append(c)
		elif len(opening_brackets) == 0:
			break
		else:
			index = GetIndex(ClosingBrackets, c)
			last_open_bracket = opening_brackets.pop()
			if OpeningBrackets[index] != last_open_bracket:
				return Scores[index], opening_brackets
	return 0, opening_brackets

def ProcessRemainder(remainder):
	score = 0
	while len(remainder) > 0:
		entry = remainder.pop()
		score *= 5
		score += GetIndex(OpeningBrackets, entry) + 1

	return score

data = ReadData()
total_score = 0
remainder_scores = []
for chunk in data:
	score, remaining = ProcessChunk(chunk)
	total_score += score
	if score == 0:
		remainder_scores.append(ProcessRemainder(remaining))


print(total_score)
remainder_scores.sort()
halfway = int(len(remainder_scores)/2)
print(str(remainder_scores[halfway]))