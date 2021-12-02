# PART ONE

import os

scriptsPath = os.path.dirname(os.path.realpath(__file__))
os.chdir(scriptsPath)
print("\nCurrent working directory: " + str(os.getcwd()) + "\n")

rawFile = open("input.txt")
contents = rawFile.read()
data = contents.splitlines()

horizontal = 0
depth = 0

for i in data:
    instance = i.split(" ")
    move = instance[0]
    magnitude = int(instance[1])

    print(move, end="---")
    print(magnitude)

    if move == "forward":
        horizontal += int(instance[1])
    if move == "down":
        depth += int(instance[1])
    if move == "up":
        depth -= int(instance[1])

print(horizontal * depth)

# PART TWO

import os

scriptsPath = os.path.dirname(os.path.realpath(__file__))
os.chdir(scriptsPath)
print("\nCurrent working directory: " + str(os.getcwd()) + "\n")

rawFile = open("input.txt")
contents = rawFile.read()
data = contents.splitlines()

horizontal = 0
depth = 0
aim = 0

for i in data:
    instance = i.split(" ")
    move = instance[0]
    magnitude = int(instance[1])

    print(move, end="---")
    print(magnitude)

    if move == "forward":
        horizontal += int(instance[1])
        depth += aim * int(instance[1])
    if move == "down":
        aim += int(instance[1])
    if move == "up":
        aim -= int(instance[1])

print(horizontal * depth)
