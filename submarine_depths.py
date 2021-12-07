import os 

def simple_measure():
    previous_measurement = 0
    depth_increases = -1
    with open(os.getcwd() + "/data/submarine_depths.txt", "r") as data:
        for raw_new_measurement in data:
            new_measurement = int(raw_new_measurement)
            if new_measurement > previous_measurement:
                depth_increases = depth_increases + 1
            previous_measurement = new_measurement

    print(depth_increases)

def complex_measure():
    slide_number = 3
    measures = [0,0,0]
    count = 0
    previous_measure = 0
    increases = 0
    with open(os.getcwd() + "/data/submarine_depths.txt", "r") as data:
        for raw_new_measurement in data:
            new_measurement = int(raw_new_measurement)

            index = count % slide_number

            i = 0
            if count < slide_number:
                while i <= index:
                    measures[i] = measures[i] + new_measurement
                    i = i + 1
            else:
                while i < slide_number:
                    if i == index and count >= slide_number:
                        current_measure = measures[index]
                        if previous_measure > 0:
                            if current_measure > previous_measure:
                                increases = increases + 1
                        previous_measure = current_measure

                        measures[index] = 0
                    measures[i] = measures[i] + new_measurement
                    i = i + 1

            count = count + 1
        current_measure = measures[count % slide_number]
        if previous_measure > 0 and current_measure > previous_measure:
            increases = increases + 1
        print(increases)

complex_measure()