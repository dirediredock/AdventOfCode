# PART ONE

import os

scriptsPath = os.path.dirname(os.path.realpath(__file__))
os.chdir(scriptsPath)
print("\nCurrent working directory: " + str(os.getcwd()) + "\n")

rawFile = open("input.txt")
contents = rawFile.read()
data = contents.split("\n")
data = data[:-1]

# data = [
#     "2199943210",
#     "3987894921",
#     "9856789892",
#     "8767896789",
#     "9899965678",
# ]

array = []
for i in data:
    row = []
    for j in i:
        row.append(int(j))
    array.append(row)

max_Y = len(array)
max_X = len(array[0])

min_Y = -1
min_X = -1

print(max_Y, max_X, end="\n\n")

outputValues = []
outputX = []
outputY = []

locY = min_Y
for row in array:
    locY += 1
    locX = min_X
    for col in row:
        locX += 1

        index_U = locY - 1
        index_D = locY + 1
        index_L = locX - 1
        index_R = locX + 1

        value = array[locY][locX]

        print("value", value, "| X", locX, "Y", locY, end="")

        neighborhood = []

        if index_U > min_Y:
            value_U = array[index_U][locX]
            neighborhood.append(value_U)
        if index_D < max_Y:
            value_D = array[index_D][locX]
            neighborhood.append(value_D)
        if index_L > min_X:
            value_L = array[locY][index_L]
            neighborhood.append(value_L)
        if index_R < max_X:
            value_R = array[locY][index_R]
            neighborhood.append(value_R)

        failCount = 0
        for i in neighborhood:
            if value >= i:
                failCount += 1

        if failCount == 0:
            outputValues.append(value)
            outputY.append(locY)
            outputX.append(locX)

        print(" |", neighborhood)

print()

print("Z", outputValues)
print("X", outputX)
print("Y", outputY)

riskLevel = 0

for i in outputValues:
    riskLevel += i + 1

print("\nRisk Level:", riskLevel)

# BONUS VISUALIZATION

import matplotlib.pyplot as plt
import matplotlib as mpl
import os

mpl.use("Agg")

scriptsPath = os.path.dirname(os.path.realpath(__file__))
os.chdir(scriptsPath)
print("\nCurrent working directory: " + str(os.getcwd()) + "\n")

rawFile = open("input.txt")
contents = rawFile.read()
data = contents.split("\n")

# data = [
#     "2199943210",
#     "3987894921",
#     "9856789892",
#     "8767896789",
#     "9899965678",
# ]

array = []
for i in data[:-1]:
    row = []
    for j in i:
        row.append(int(j))
    array.append(row)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
fig.patch.set_facecolor("k")

ax.pcolor(array, cmap="inferno_r")

edge = 0.05

plt.gca().set_position([edge, edge, 1 - (edge * 2), 1 - (edge * 2)])
plt.axis("off")

plt.savefig("Day09_SmokeBasin", dpi=300)
