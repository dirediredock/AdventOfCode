# PART ONE

import os

scriptsPath = os.path.dirname(os.path.realpath(__file__))
os.chdir(scriptsPath)
print("\nCurrent working directory: " + str(os.getcwd()) + "\n")

rawFile = open("input.txt")
contents = rawFile.read()
data = contents.splitlines()

dataLength = 0
for i in data:
    dataLength += 1

counts = []
for i in range(len(data[0])):
    counts.append([])

for number in data:
    for i in range(len(number)):
        counts[i].append(number[i])

freq1 = []

for i in range(len(counts)):
    freq1.append(int(counts[i].count("1")))

freq0 = []

for i in range(len(counts)):
    freq0.append(dataLength - freq1[i])

gamma = ""
epsilon = ""

for i in range(len(freq1)):
    ones = freq1[i]
    zeros = freq0[i]

    if ones > zeros:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"


def binaryToDecimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    return decimal


print(binaryToDecimal(gamma) * binaryToDecimal(epsilon))
