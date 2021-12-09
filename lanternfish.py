import os

def ReadData():
     with open(os.getcwd() + "/data/lanternfish.txt") as file:
        for line in file:
            return line.split(",")


def Main():
    initial_values = ReadData()

    lanternfish = [0,0,0,0,0,0,0,0,0]
    for value in initial_values:
        fish_age = int(value)
        lanternfish[fish_age] += 1

    days = 1
    while days <= 256:    
        new_fish = lanternfish[0]

        i = 0
        while i < len(lanternfish) - 1:
            lanternfish[i] = lanternfish[i + 1]
            i += 1

        lanternfish[6] += new_fish
        lanternfish[8] = new_fish  
        
        # print("DAY: " + str(days) + str(lanternfish))
        # total = 0
        # for i in lanternfish:
        #     total += i
        # print("TOTAL: " + str(total))  

        days += 1
    
    total = 0
    for i in lanternfish:
        total += i
    print(total)

Main()