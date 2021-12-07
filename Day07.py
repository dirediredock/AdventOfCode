# PART ONE

import os

scriptsPath = os.path.dirname(os.path.realpath(__file__))
os.chdir(scriptsPath)
print("\nCurrent working directory: " + str(os.getcwd()) + "\n")

rawFile = open("input.txt")
contents = rawFile.read()
items = contents.split(",")

data = []

for i in items:
    data.append(int(i))

print(data)

from statistics import median

# data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

pivot = median(data)

distance = []
for i in data:
    distance.append(abs(i - pivot))

sum = 0
for i in distance:
    sum += i

print(int(sum))
