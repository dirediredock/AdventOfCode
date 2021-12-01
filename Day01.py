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

print(count)
