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

# PART TWO

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


def binaryToDecimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    return decimal


def isMostCommonBit_ONE(data, columnLoc):

    howMany_ones = 0
    howMany_zero = 0

    for num in data:
        if num[columnLoc] == "1":
            howMany_ones += 1
        else:
            howMany_zero += 1

    print("one", howMany_ones, "zero", howMany_zero)

    if howMany_ones == howMany_zero:
        return True
    return howMany_ones > howMany_zero


def getOxygen():
    innerData = data.copy()

    bitIndex = 0
    while len(innerData) > 1 and bitIndex < len(innerData[0]):
        mostCommonBit = "0"
        if isMostCommonBit_ONE(innerData, bitIndex):
            mostCommonBit = "1"
        newData = []
        for id in innerData:
            if id[bitIndex] == mostCommonBit:
                newData.append(id)
        innerData = newData
        bitIndex += 1
        print(innerData)

    return binaryToDecimal(innerData[0])


def getCarbon():
    innerData = data.copy()

    bitIndex = 0
    while len(innerData) > 1 and bitIndex < len(innerData[0]):
        leastCommonBit = "1"
        if isMostCommonBit_ONE(innerData, bitIndex):
            leastCommonBit = "0"
        newData = []
        for id in innerData:
            if id[bitIndex] == leastCommonBit:
                newData.append(id)
        innerData = newData
        bitIndex += 1
        print(innerData)

    return binaryToDecimal(innerData[0])


oxygen = getOxygen()
carbon = getCarbon()
lifeSupport = oxygen * carbon

print("oxygen", oxygen, "carbon", carbon, "lifeSupport", lifeSupport)

