import os 

def ReadData():
	with open(os.getcwd() + "/data/whalebetrayal.txt") as file:
		for line in file:
			return line.split(",")

def BasicEvalPosition(crab_positions, position_to_eval):
	fuel_cost = 0
	for position in crab_positions:
		fuel_cost += abs(int(position) - position_to_eval)
	return fuel_cost

def ComplexEvalPosition(crab_positions, position_to_eval):
	fuel_cost = 0
	for position in crab_positions:
		steps = abs(int(position) - position_to_eval)
		while steps > 0:
			fuel_cost += steps
			steps -= 1
	return fuel_cost

crab_positions = ReadData()
first_val = int(crab_positions[0])
min_pos = first_val
max_pos = first_val
for position in crab_positions:
	min_pos = min(int(position), min_pos)
	max_pos = max(int(position), max_pos)
i = min_pos
best_position = -1
best_fuel_cost = -1
count = 0

while i < max_pos:
	fuel_cost = ComplexEvalPosition(crab_positions, i)
	#fuel_cost = EvalPosition(crab_positions, int(position))
	if fuel_cost < best_fuel_cost or best_fuel_cost == -1:
		best_position = count
		best_fuel_cost = fuel_cost
	i += 1
print(best_fuel_cost)