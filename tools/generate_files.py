import os

filename = input("Please type the name of the files you want to create \n")


with open(os.getcwd() + "/" + filename + ".py", "w") as file:
    file.write("import os \n\n")
    file.write("def ReadData():\n")
    file.write("\tdata = []\n")
    file.write("\twith open(os.getcwd() + '/data/" + filename + "test.txt') as file:\n") 
    file.write("\t\tfor line in file:\n")
    file.write("\treturn data")

    file.write("\n\n\ndata = ReadData()\nprint(str(data))")
    pass

data_filepath = os.getcwd() + "/data/"
with open(data_filepath + filename + "_test.txt", "w+") as file:
    pass

with open(data_filepath + filename + ".txt", "w") as file:
    pass