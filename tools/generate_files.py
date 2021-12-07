import os

filename = input("Please type the name of the files you want to create \n")


with open(os.getcwd() + "/" + filename + ".py", "w") as file:
    pass

data_filepath = os.getcwd() + "/data/"
with open(data_filepath + filename + "_test.txt", "w+") as file:
    pass

with open(data_filepath + filename + ".txt", "w") as file:
    pass