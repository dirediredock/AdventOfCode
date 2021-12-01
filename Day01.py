# PART ONE

import os

scriptsPath = os.path.dirname(os.path.realpath(__file__))
os.chdir(scriptsPath)
print("\nCurrent working directory: " + str(os.getcwd()) + "\n")

rawFile = open("input.txt")
contents = rawFile.read()
list = contents.splitlines()

count = 0

for i in range(len(list)):
    if i == 0:
        continue
    A = list[i - 1]
    B = list[i]
    diff = int(A) - int(B)

    if diff < 0:
        count += 1

print("\nTotal count:", count, "\n")

# PART TWO

import os

scriptsPath = os.path.dirname(os.path.realpath(__file__))
os.chdir(scriptsPath)
print("\nCurrent working directory: " + str(os.getcwd()) + "\n")

rawFile = open("input.txt")
contents = rawFile.read()
data = contents.splitlines()

count = 0

sumList = []
iteration = -1

for i in range(len(data)):
    if i < 2:
        continue
    iteration += 1
    sum = int(data[i - 2]) + int(data[i - 1]) + int(data[i])
    sumList.append(sum)

    print(data[i], end=" ")
    print(data[i - 1], end=" ")
    print(data[i - 2], "---> Sum:", sum)

    print(sumList[iteration])

    diff = sumList[iteration - 1] - sumList[iteration]

    if diff < 0:
        count += 1

print("\nTotal count:", count, "\n")
