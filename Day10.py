# PART ONE

class Stack:
    def __init__(self):
        self.items = []
    def enStack(self, item):
        self.items.insert(0, item)
    def deStack(self):
        return self.items.pop(0)
    def printStack(self):
        return self.items

def illegal_score(string):
    S = Stack()
    for i in string:
        if i == "(":
            S.enStack(i)
        if i == "[":
            S.enStack(i)
        if i == "{":
            S.enStack(i)
        if i == "<":
            S.enStack(i)
        if i == ")":
            if S.printStack()[0] == "(":
                S.deStack()
            else:
                return 3
        if i == "]":
            if S.printStack()[0] == "[":
                S.deStack()
            else:
                return 57
        if i == "}":
            if S.printStack()[0] == "{":
                S.deStack()
            else:
                return 1197
        if i == ">":
            if S.printStack()[0] == "<":
                S.deStack()
            else:
                return 25137

import os

scriptsPath = os.path.dirname(os.path.realpath(__file__))
os.chdir(scriptsPath)
print("\nCurrent working directory: " + str(os.getcwd()) + "\n")

rawFile = open("input.txt")
contents = rawFile.read()
data = contents.splitlines()

# data = [
#     "[({(<(())[]>[[{[]{<()<>>",
#     "[(()[<>])]({[<{<<[]>>(",
#     "{([(<{}[<>[]}>{[]{[(<()>",
#     "(((({<>}<{<{<>}{[]{[]{}",
#     "[[<[([]))<([[{}[[()]]]",
#     "[{[{({}]{}}([{[{{{}}([]",
#     "{<[[]]>}<{[{[{[]{()[[[]",
#     "[<(<(<(<{}))><([]([]()",
#     "<{([([[(<>()){}]>(<<{{",
#     "<{([{{}}[<[[[<>{}]]]>[]]",
# ]

sum_score = 0

for i in data:
    score = illegal_score(i)
    if score != None:
        sum_score += score

print(sum_score)

# PART TWO

class Stack:
    def __init__(self):
        self.items = []
    def enStack(self, item):
        self.items.insert(0, item)
    def deStack(self):
        return self.items.pop(0)
    def printStack(self):
        return self.items
    def hasItems(self):
        return len(self.items) > 0

def illegal_index(string):
    S = Stack()
    for i in string:
        if i == "(":
            S.enStack(i)
        if i == "[":
            S.enStack(i)
        if i == "{":
            S.enStack(i)
        if i == "<":
            S.enStack(i)
        if i == ")":
            if S.printStack()[0] == "(":
                S.deStack()
            else:
                return "illegal!"
        if i == "]":
            if S.printStack()[0] == "[":
                S.deStack()
            else:
                return "illegal!"
        if i == "}":
            if S.printStack()[0] == "{":
                S.deStack()
            else:
                return "illegal!"
        if i == ">":
            if S.printStack()[0] == "<":
                S.deStack()
            else:
                return "illegal!"

import os

scriptsPath = os.path.dirname(os.path.realpath(__file__))
os.chdir(scriptsPath)
print("\nCurrent working directory: " + str(os.getcwd()) + "\n")

rawFile = open("input.txt")
contents = rawFile.read()
data = contents.splitlines()

# data = [
#     "[({(<(())[]>[[{[]{<()<>>",
#     "[(()[<>])]({[<{<<[]>>(",
#     "{([(<{}[<>[]}>{[]{[(<()>",
#     "(((({<>}<{<{<>}{[]{[]{}",
#     "[[<[([]))<([[{}[[()]]]",
#     "[{[{({}]{}}([{[{{{}}([]",
#     "{<[[]]>}<{[{[{[]{()[[[]",
#     "[<(<(<(<{}))><([]([]()",
#     "<{([([[(<>()){}]>(<<{{",
#     "<{([{{}}[<[[[<>{}]]]>[]]",
# ]

new_data = []
for i in data:
    if illegal_index(i) != "illegal!":
        new_data.append(i)

def missing_brackets(string):
    S = Stack()
    for i in string:
        if i == "(":
            S.enStack(i)
        if i == "[":
            S.enStack(i)
        if i == "{":
            S.enStack(i)
        if i == "<":
            S.enStack(i)
        if i == ")":
            if S.printStack()[0] == "(":
                S.deStack()
        if i == "]":
            if S.printStack()[0] == "[":
                S.deStack()
        if i == "}":
            if S.printStack()[0] == "{":
                S.deStack()
        if i == ">":
            if S.printStack()[0] == "<":
                S.deStack()
    flipped = []
    score = 0
    for i in S.printStack():
        if i == "(":
            score *= 5
            score += 1
            flipped.append(")")
        if i == "[":
            score *= 5
            score += 2
            flipped.append("]")
        if i == "{":
            score *= 5
            score += 3
            flipped.append("}")
        if i == "<":
            score *= 5
            score += 4
            flipped.append(">")
    return flipped, score

scores = []
for i in new_data:
    dummy, score = missing_brackets(i)
    scores.append(score)

winner = sorted(scores)[len(scores) // 2]

print(winner)
