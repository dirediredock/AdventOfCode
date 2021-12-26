# PART ONE

import os

scriptsPath = os.path.dirname(os.path.realpath(__file__))
os.chdir(scriptsPath)
print("\nCurrent working directory: " + str(os.getcwd()) + "\n")

rawFile = open("input.txt")
contents = rawFile.read()
data = contents.splitlines()

# data = [
#     1721,
#     979,
#     366,
#     299,
#     675,
#     1456,
# ]

for i in data:
    for j in data:
        if int(i) + int(j) == 2020:
            print(int(i) * int(j))
            
# PART TWO

import os

scriptsPath = os.path.dirname(os.path.realpath(__file__))
os.chdir(scriptsPath)
print("\nCurrent working directory: " + str(os.getcwd()) + "\n")

rawFile = open("input.txt")
contents = rawFile.read()
data = contents.splitlines()

# data = [
#     1721,
#     979,
#     366,
#     299,
#     675,
#     1456,
# ]

def account(list):
    for i in list:
        for j in list:
            for k in list:
                if int(i) + int(j) + int(k) == 2020:
                    return int(i) * int(j) * int(k)

print(account(data))
