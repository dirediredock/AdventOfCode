# BONUS

import matplotlib.pyplot as plt
import os

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
plt.show()
