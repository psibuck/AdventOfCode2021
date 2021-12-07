import os

def get_value(input):
    if input == 1:
        return 1
    return -1
    
def from_binary(array):
    num = 0
    for i in range(len(array)):
        num = num + int(array[i])
        num = num * 2
    return num / 2

def basic_diagnostics():
    bgamma_rate = []
    bepsilon_rate = []
    counts = []
    with open(os.getcwd() + "/data/binary_diagnostics.txt",'r') as data:
        for entry in data:
            index = 0
            for value in entry:
                if value != "\n":
                    if index > len(counts) - 1:
                        counts.append(0)
                    counts[index] = counts[index] + get_value(int(value))
                index = index + 1
            print(counts)
        for count in counts:
            if count > 0:
                bgamma_rate.append(1)
                bepsilon_rate.append(0)
            else:
                bgamma_rate.append(0)
                bepsilon_rate.append(1)

    gamma_rate = int(from_binary(bgamma_rate))
    epsilon_rate = int(from_binary(bepsilon_rate))
    print(gamma_rate * epsilon_rate)

def filter_list(list, index, comparator):
    ones = []
    zeros = []
    for entry in list:
        if index < len(entry):
            value = entry[index]
            if value != "\n":
                if int(value) == 1:
                    ones.append(entry)
                else:
                    zeros.append(entry)
    if len(ones) >= len(zeros):
        return ones, zeros
    return zeros,ones



def advanced_diagnostics():
    oxygen = []
    co2 = []
    with open(os.getcwd() + "/data/binary_diagnostics.txt",'r') as data:
        data_list = data.read().splitlines()
    
        oxygen = data_list
        co2 = data_list
    index = 0
    while len(co2) != 1 or len(oxygen) != 1:
        if len(oxygen) != 1:
            oxygen,_ = filter_list(oxygen, index,1)
        if len(co2) != 1:
            _,co2 = filter_list(co2, index,0)
        index += 1

    oxygen_generator_rating = from_binary(oxygen[0])
    co2_scrubbing_rating = from_binary(co2[0])

    print(oxygen_generator_rating * co2_scrubbing_rating)


    
advanced_diagnostics()