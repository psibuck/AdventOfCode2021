import os

def ReadData():
    vectors = []
    with open(os.getcwd() + "/data/hydrothermal.txt") as file:
        for line in file:
            entry = line.strip("\n")
            entry = entry.split(" -> ")
            vectors.append(entry)
    return vectors

class Line:
    def __init__(self):
        self.values = []

    def SingleCoord(self, coord):
        while coord >= len(self.values):
            self.values.append(0)

        self.values[coord] += 1
        if self.values[coord] == 2:
            return 1
        return 0

    def Process(self, coord1, coord2):
        i = min(coord1, coord2)
        count = 0
        while i <= max(coord1, coord2):
            count += self.SingleCoord(i)
            i += 1
        return count

class Application:

    def __init__(self):
        self.overlaps = 0
        self.count = []

    def ProcessXCoordinate(self, y, x1, x2):
        while len(self.count) <= max(x1,x2):
            self.count.append(0)
        
        i = min(x1,x2)
        while i <= max(x1,x2):
            entry = self.count[i]
            if entry == 0:
                entry = Line()
                self.count[i] = entry
            self.overlaps += entry.SingleCoord(y)
            i += 1

    def ProcessYCoordinate(self, x, y1, y2):
        while x >= len(self.count):
            self.count.append(0)
        
        entry = self.count[x]
        if entry == 0:
            entry = Line()
            self.count[x] = entry
        
        self.overlaps += entry.Process(y1, y2)
    
    def ProcessDiagCoordinate(self, x1,x2,y1,y2):
        xcrement = 1
        ycrement = 1
        if x2 < x1:
            xcrement = -1
        if y2 < y1:
            ycrement = -1
    
        while True:
            self.ProcessXCoordinate(y1, x1, x1)


            if x1 == x2 and y1 == y2:
                break
            x1 += xcrement
            y1 += ycrement


def SimpleThermos():
    app = Application()
    data = ReadData()
    for entry in data:
        # print("LOOP")
        # for value in app.count:
        #     if value == 0:
        #         print(0)
        #     else:
        #         print(value.values)
        vec1 = entry[0]
        vec2 = entry[1]
        
        initcoords = vec1.split(",")
        endcoords = vec2.split(",")
        x1 = int(initcoords[0])
        x2 = int(endcoords[0])
        y1 = int(initcoords[1])
        y2 = int(endcoords[1])

        if x1 == x2:
            app.ProcessYCoordinate(x1, y1, y2)
        elif y1 == y2:
            app.ProcessXCoordinate(y1, x1, x2)
        else:
            app.ProcessDiagCoordinate(x1,x2,y1,y2)

    print(app.overlaps)
    # overlaps = 0
    # for data in app.count:
    #     if data == 0:
    #         continue
    #     for count in data.values:
    #         if count >= 2:
    #             overlaps += 1

  #  print(overlaps)

SimpleThermos()