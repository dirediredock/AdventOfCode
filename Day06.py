# PART ONE

import os

scriptsPath = os.path.dirname(os.path.realpath(__file__))
os.chdir(scriptsPath)
print("\nCurrent working directory: " + str(os.getcwd()) + "\n")

rawFile = open("input.txt")
contents = rawFile.read()

items = contents.split(",")

state = []

for i in items:
    state.append(int(i[0]))

print(state)

# state = [3, 4, 3, 1, 2]

# print("Initial sate:", state)

for i in range(80):

    nextState = []
    addons = []

    for fish in state:
        if fish == 0:
            nextState.append(6)
            addons.append(8)
        else:
            nextState.append(fish - 1)

    state = nextState.copy()

    for j in addons:
        state.append(j)

    # print("Day", str(i + 1) + ":", state)

print(len(state))

# PART TWO

