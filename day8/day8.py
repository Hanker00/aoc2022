with open("day8/day8.txt") as f:
    rows = f.read().split("\n")

print(list(rows[0]))
visible = 0
for row in range(1, len(rows) - 1):
    for cell in range(1, len(rows[row]) - 1):
        # To the left
        current_cell_val = rows[row][cell]
        print(list(rows[row])[:cell])
        if(max((list(rows[row])[:cell])) < current_cell_val):
            visible += 1
            continue
        # To the right
        elif(max(rows[row][cell:len(rows[row])]) < current_cell_val):
            visible += 1
            continue
print(visible)