import os 

def ReadData():
	coords = []
	instructions = []
	in_instructions = False
	with open(os.getcwd() + '/data/transparent_origami.txt') as file:
		for line in file:
			if line == "\n":
				in_instructions = True
			else:
				line = line.strip("\n")
				if in_instructions:
					line = line.strip("fold along ")
					instructions.append(line)	
				elif line != "\n":
					coordinates = line.split(",")
					coords.append(coordinates)
	return coords, instructions

def CreateGrid(coords):
	grid = []
	for entry in coords:
		x = int(entry[0])
		y = int(entry[1])
		while y >= len(grid):
			grid.append(["."])
		
		for col in grid:
			while x >= len(col):
				col.append(".")

		grid[y][x] = "#"		
		 
	return grid

def PrintGrid(grid):
	for y in range(len(grid)):
		line = ""
		for x in range(len(grid[y])):
			line += str(grid[y][x])
		print(line)

def GetFlip(flipstring):
	flip = flipstring.split("=")
	if flip[0] == "x":
		flip[0] = 0
	else:
		flip[0] = 1
	return [flip[0], int(flip[1])]

def GetFlipCoordinates(grid, flip):
	xoffset = 0
	yoffset = 0
	if flip[0] == 1:
		yoffset = flip[1]
	else:
		xoffset = flip[1] 
	
	coords = []
	for y in range(yoffset, len(grid)):
		line = ""
		for x in range(xoffset, len(grid[y])):
			if grid[y][x] == "#":
				coords.append([x,y])
	return coords

def StripFlippedSection(grid, flip):
	if flip[0] == 1:
		return grid[:flip[1]]
	else:
		for i in range(len(grid)):
			grid[i] = grid[i][:flip[1]]
		return grid
	return

def GetFlippedCoord(coord, flip):
	if flip[0] == 1:
		coord[1] = flip[1] - (coord[1] - flip[1]) 
	else:
		coord[0] = flip[1] - (coord[0] - flip[1]) 
	return coord

def ProcessFlips(coords, grid, flip):
	for coord in coords:
		flipped = GetFlippedCoord(coord, flip)
		grid[flipped[1]][flipped[0]] = "#"

	return grid

coords, instructions = ReadData()
grid = CreateGrid(coords)

for instruction in instructions:
	flip = GetFlip(instruction)
	flip_coords = GetFlipCoordinates(grid, flip)
	grid = StripFlippedSection(grid, flip)
	grid = ProcessFlips(flip_coords, grid, flip)

PrintGrid(grid)

count = 0
for i in range(len(grid)):
	for j in range(len(grid[i])):
		if grid[i][j] == "#":
			count += 1
print(count)