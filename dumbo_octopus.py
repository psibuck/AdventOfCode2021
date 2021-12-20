import os 

class Octopus:

	def __init__ (self, energy_level, i, j):
		self.energy_level = energy_level
		self.last_flashed = 101
		self.i = i
		self.j = j
	
	def Flash(self, step):
		self.last_flashed = step

	def Energise(self):
		self.energy_level += 1

	def HasFlashed(self, steps):
		return steps == self.last_flashed

	def ShouldFlash(self, steps):
		return not self.HasFlashed(steps) and self.energy_level > 9

	def __str__(self):
		return str(self.energy_level)

def PrintBoard(data):
	for entry in data:
		line = []
		for octo in entry:
			line.append(octo.energy_level)
		print(str(line))
	print("\n")
	
def ReadData():
	data = []
	with open(os.getcwd() + '/data/dumbo_octopus.txt') as file:
		i = 0
		j = 0
		for line in file:
			octo_line = []
			line = line.strip("\n")
			for entry in line:
				octo_line.append(Octopus(int(entry), i, j))
				j += 1
			data.append(octo_line)
			j = 0
			i += 1
	return data

def IsValid(index):
	return index >= 0 and index < 10

def GetAdjacentOctopuses(octo, data):
	i = octo.i - 1
	j = octo.j - 1

	octos_out = []
	while i <= octo.i+1:
		while j <= octo.j+1:
			if IsValid(i) and IsValid(j):
				new_octo = GetOcto(i,j)
				if new_octo != octo:
					octos_out.append(new_octo)
			j += 1
		j = octo.j - 1
		i += 1

	return octos_out
	
def ProcessOcto(steps, octo, data):
	if octo.ShouldFlash(steps):
		octo.Flash(steps)
		global num_flashes
		num_flashes += 1
		adjacent_octos = GetAdjacentOctopuses(octo, data)
		for octo in adjacent_octos:
			octo.Energise()
			ProcessOcto(steps, octo, data)

def GetOcto(i,j):
	global data
	return data[i][j]

def RunNumSteps(NumSteps):
	step_number = 1
	while step_number != NumSteps:

		# print("Step: " + str(100 - steps))
		# PrintBoard(data)

		for i in range(len(data)):
			for j in range(len(data)):
				octo = GetOcto(i,j)

				if not octo.HasFlashed(step_number):
					octo.Energise()

				ProcessOcto(step_number, octo, data)

		count = 0
		for i in range(len(data)):
			for j in range(len(data)):
				octo = GetOcto(i,j)
				if octo.HasFlashed(step_number):
					octo.energy_level = 0
					count += 1
					if count == 100:
						return step_number

		step_number += 1


num_flashes = 0
steps = 100
data = ReadData()

# RunNumSteps(101)
# print(num_flashes)

solution = RunNumSteps(-1)
print(solution)