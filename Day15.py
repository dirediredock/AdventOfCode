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
#     "1163751742",
#     "1381373672",
#     "2136511328",
#     "3694931569",
#     "7463417111",
#     "1319128137",
#     "1359912421",
#     "3125421639",
#     "1293138521",
#     "2311944581",
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

ax.pcolor(array, cmap="inferno")

edge = 0.05

plt.gca().set_position([edge, edge, 1 - (edge * 2), 1 - (edge * 2)])
plt.axis("off")

plt.show()

plt.savefig("Day15_Chiton", dpi=300)
