import os 


class CaveNode():

	def __init__(self, name):
		self.name = name
		self.connections = []
		self.is_big = self.name.isupper()

	def AddConnection(self, connection):
		self.connections.append(connection)

	def __str__(self):
		return self.name

def GetCaveNode(name):
	global data
	for cave in data:
		if cave.name == name:
			return cave
	new_cave = CaveNode(name)
	data.append(new_cave)
	return new_cave


data = []
def ReadData():
	with open(os.getcwd() + '/data/passage_pathing.txt') as file:
		for line in file:	
			line = line.strip("\n")
			caves = line.split("-")
			
			for i in range(2):
				cave = GetCaveNode(caves[i])
				cave.AddConnection(GetCaveNode(caves[1-i]))

ReadData()

count = 0
cave_path = []

def HasDouble(cave_path):
	lowers = []
	for entry in cave_path:
		if entry.islower():
			if entry in lowers:
				return True
			else:
				lowers.append(entry)
	return False


def print_connections(cave):
	global cave_path

	cave_path.append(str(cave))

	for connection in cave.connections:
		
		if connection.name == "end":
			cave_path.append(connection.name)
			global count
			count += 1
			print("Reached end!")
			print(cave_path)
			cave_path.pop()
			continue

		if connection.name == "start" or not connection.is_big and connection.name in cave_path and HasDouble(cave_path):

			#print("Dead end at: " + str(connection))
			continue

		print_connections(connection)
	cave_path.pop()
		

for cave in data:
	if cave.name == "start":
		print_connections(cave)
		break
print(count)