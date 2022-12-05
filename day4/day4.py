with open("day4\day4.txt") as f:
    lines = f.read()
    lines = lines.split("\n")

count = 0
print(lines)
for pair in lines:
    pair1, pair2 = pair.split(',')
    pair1from, pair1to = pair1.split('-')
    pair2from, pair2to = pair2.split('-')
    pair1 = set(range(int(pair1from), int(pair1to) + 1))
    pair2 = set(range(int(pair2from), int(pair2to) + 1))
    if(set(pair1) & set(pair2)):
        count += 1
print(count)