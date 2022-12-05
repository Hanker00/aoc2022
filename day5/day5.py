import numpy as np
with open("day5\day5.txt") as f:
    crates, instructions = f.read().split("\n\n")
    crates = crates.replace("    ", "  *  ").replace(" ", "").replace("[", "").replace("]", "").split("\n")
crates.pop()
multiple_stacks = []
print(crates)
for i in range(len(crates[0])):
    stack = []
    for level in crates:
        if(level[i] != "*"):
            stack.append(level[i])
    multiple_stacks.append(stack[::-1])
print(multiple_stacks)

instructions = instructions.replace("move ", "").replace("from", "").replace("to", "").split("\n")
for i in instructions:
    instruction = "".join(i).split()
    print(instruction)
    
    same_order = []
    for i in range(int(instruction[0])):
        toInsert = multiple_stacks[int(instruction[1]) - 1].pop()
        same_order.insert(0, toInsert)
    for i in same_order:
        multiple_stacks[int(instruction[2]) - 1].append(i)

all_top = ""
for stack in multiple_stacks:
    all_top = all_top + stack.pop()
print(all_top)

    


