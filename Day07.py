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

# PART TWO

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

# data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

pivotA = sum(data) // len(data)
pivotB = (sum(data) // len(data)) + 1

# Pivot here is mean with floor division, so there are two versions

def calculateDistance(data, pivot):
    sum = 0
    for i in data:
        distance = abs(i - pivot)
        sum += (distance * (distance + 1)) // 2
    return sum

answer = min(calculateDistance(data, pivotA), calculateDistance(data, pivotB))

print(answer)
