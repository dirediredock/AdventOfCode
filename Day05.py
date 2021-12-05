# PART ONE

import os

scriptsPath = os.path.dirname(os.path.realpath(__file__))
os.chdir(scriptsPath)
print("\nCurrent working directory: " + str(os.getcwd()) + "\n")

rawFile = open("input.txt")
contents = rawFile.read()
data = contents.splitlines()

# data = [
#     "0,9 -> 5,9",
#     "8,0 -> 0,8",
#     "9,4 -> 3,4",
#     "2,2 -> 2,1",
#     "7,0 -> 7,4",
#     "6,4 -> 2,0",
#     "0,9 -> 2,9",
#     "3,4 -> 1,4",
#     "0,0 -> 8,8",
#     "5,5 -> 8,2",
# ]


def splitter(sequence, delimiter):
    splitA = []
    splitB = []
    for i in sequence:
        split = i.split(delimiter)
        splitA.append(split[0])
        splitB.append(split[1])
    return splitA, splitB


splitA, splitB = splitter(data, " -> ")

x1, y1 = splitter(splitA, ",")
x2, y2 = splitter(splitB, ",")

pointsA = []
pointsB = []

for i in range(len(x1)):
    pointsA.append([int(x1[i]), int(y1[i])])
    pointsB.append([int(x2[i]), int(y2[i])])

points = {}
maxGridX = 0
maxGridY = 0
for i in range(len(pointsA)):
    pointA = pointsA[i]
    pointB = pointsB[i]
    linePoints = []
    if pointA[0] == pointB[0]:
        # veritcal line
        x = pointA[0]
        maxY = max([pointA[1], pointB[1]])
        minY = min([pointA[1], pointB[1]])
        maxGridX = max([x, maxGridX])
        maxGridY = max([maxGridY, maxY])
        for y in range(minY, maxY + 1):
            linePoints.append((x, y))
    elif pointA[1] == pointB[1]:
        # horizontal line
        y = pointA[1]
        maxX = max([pointA[0], pointB[0]])
        minX = min([pointA[0], pointB[0]])
        maxGridX = max([maxX, maxGridX])
        maxGridY = max([y, maxGridY])
        for x in range(minX, maxX + 1):
            linePoints.append((x, y))
    for point in linePoints:
        if points.get(point):
            points[point] += 1
        else:
            points[point] = 1

for y in range(maxGridY + 1):
    for x in range(maxGridX + 1):
        pointCount = points.get((x, y))
        if pointCount != None:
            print(pointCount, end="")
        else:
            print(".", end="")
    print()

dangerPointCount = 0
for count in points.values():
    if count > 1:
        dangerPointCount += 1

print(dangerPointCount)

# PART TWO

import os

scriptsPath = os.path.dirname(os.path.realpath(__file__))
os.chdir(scriptsPath)
print("\nCurrent working directory: " + str(os.getcwd()) + "\n")

rawFile = open("input.txt")
contents = rawFile.read()
data = contents.splitlines()


def splitter(sequence, delimiter):
    splitA = []
    splitB = []
    for i in sequence:
        split = i.split(delimiter)
        splitA.append(split[0])
        splitB.append(split[1])
    return splitA, splitB


splitA, splitB = splitter(data, " -> ")

x1, y1 = splitter(splitA, ",")
x2, y2 = splitter(splitB, ",")

pointsA = []
pointsB = []

for i in range(len(x1)):
    pointsA.append([int(x1[i]), int(y1[i])])
    pointsB.append([int(x2[i]), int(y2[i])])

points = {}
maxGridX = 0
maxGridY = 0
for i in range(len(pointsA)):
    pointA = pointsA[i]
    pointB = pointsB[i]
    linePoints = []
    if pointA[0] == pointB[0]:
        # veritcal line
        x = pointA[0]
        maxY = max([pointA[1], pointB[1]])
        minY = min([pointA[1], pointB[1]])
        maxGridX = max([x, maxGridX])
        maxGridY = max([maxY, maxGridY])
        for y in range(minY, maxY + 1):
            linePoints.append((x, y))
    elif pointA[1] == pointB[1]:
        # horizontal line
        y = pointA[1]
        maxX = max([pointA[0], pointB[0]])
        minX = min([pointA[0], pointB[0]])
        maxGridX = max([maxX, maxGridX])
        maxGridY = max([y, maxGridY])
        for x in range(minX, maxX + 1):
            linePoints.append((x, y))
    else:
        # diagonal line
        startX = pointA[0]
        startY = pointA[1]
        endX = pointB[0]
        endY = pointB[1]

        xIsBackwards = endX < startX
        yIsBackwards = endY < startY
        maxGridX = max([startX, endX, maxGridX])
        maxGridY = max([startX, endX, maxGridY])

        y = startY

        for x in range(
            startX, endX + (-1 if xIsBackwards else 1), -1 if xIsBackwards else 1
        ):
            linePoints.append((x, y))
            y = (y - 1) if yIsBackwards else (y + 1)
    for point in linePoints:
        if points.get(point):
            points[point] += 1
        else:
            points[point] = 1

for y in range(maxGridY + 1):
    for x in range(maxGridX + 1):
        pointCount = points.get((x, y))
        if pointCount != None:
            print(pointCount, end="")
        else:
            print(".", end="")
    print()

dangerPointCount = 0
for count in points.values():
    if count > 1:
        dangerPointCount += 1

print(dangerPointCount)
