import os

FORWARD = "forward"
DOWN = "down"
UP = "up"

def simple_nav():
    hpos = 0
    depth = 0

    with open(os.getcwd() + "/data/submarine_maneouvres.txt", "r") as data:
        for order in data:
            instructions = order.split(" ")
            instruction = instructions[0]
            magnitude = int(instructions[1])

            if instruction == FORWARD:
                hpos = hpos + magnitude
            elif instruction == DOWN:
                depth = depth + magnitude
            elif instruction == UP:
                depth = depth - magnitude

    print(hpos * depth)

def complex_nav():
    hpos = 0
    depth = 0
    aim = 0

    with open(os.getcwd() + "/data/submarine_maneouvres.txt", "r") as data:
        for order in data:
            instructions = order.split(" ")
            instruction = instructions[0]
            magnitude = int(instructions[1])

            if instruction == FORWARD:
                hpos = hpos + magnitude
                depth = depth + aim * magnitude
            elif instruction == DOWN:
                aim = aim + magnitude
            elif instruction == UP:
                aim = aim - magnitude

    print(hpos * depth)

complex_nav()