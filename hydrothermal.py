import os

def ReadData():
    vectors = []
    with open(os.getcwd() + "/data/hydrothermal_test.txt") as file:
        for line in file:
            entry = line.strip("\n")
            entry = entry.split(" -> ")
            vectors.append(entry)
    print(vectors)
    return vectors

class Line:
    def __init__(self):
        self.min = -1
        self.max = -1

    def SingleCoord(self, coord):
        if coord <= self.max and coord >= self.min:
            return 1
        elif coord < self.max:
            self.max = coord


        self.max = coord
        self.min = coord

        return 0

    def Process(self, coord1, coord2):
        maxval = max(coord1, coord2)
        minval = min(coord1, coord2)
        overlaps = 0

        if self.max == -1:
            self.max = maxval
            self.min = minval
            return overlaps

        lower_bound = max(self.min, minval)
        upper_bound = min(self.max, maxval)
        overlaps = max(0, upper_bound - lower_bound + 1)

        if self.max < max:
            self.max = maxval
        if self.min > min:
            self.min = minval

        return overlaps

class Application:

    def __init__(self):
        self.overlaps = 0
        self.count = []

    def ProcessXCoordinate(self, y, x1, x2):
        xmin = min(x1, x2)
        xmax = max(x1, x2)

        while len(self.count) < xmax:
            self.count.append(0)
        
        i = xmin
        while i <= xmax:
            entry = self.count[i]
            if entry == 0:
                entry = Line()
                self.count[i] = entry
            self.overlaps += entry.SingleCoord(i)
            i += 1

    def ProcessYCoordinate(self, x, y1, y2):
        while x > len(self.count):
            self.count.append(0)
        
        entry = self.count[x]
        if entry == 0:
            entry = Line()
            self.count[x] = entry
        
        self.overlaps += entry.Process(y1, y2)

    def SimpleThermos(self):
        data = ReadData()
        for entry in data:
            vector = entry.split(",")
            vec1 = vector[0]
            vec2 = vector[1]

            x1 = vec1[0]
            x2 = vec2[0]
            y1 = vec1[1]
            y2 = vec2[1]

            if x1 == x2:
                ProcessYCoordinates(x1, y1, y2)
            else:
                ProcessXCoordinates(y1, x1, x2)


