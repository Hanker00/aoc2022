with open("day6/day6.txt") as f:
    datastream = f.read()

first_marker = 0
for i in range(len(datastream) - 13):
    if(len(set(datastream[i:i+14])) == len(datastream[i:i+14])):
        first_marker = i + 14
        break;
print(first_marker)

count = 0
for i in range(len(datastream) - 13):
    if(len(set(datastream[i:i+14])) == len(datastream[i:i+14])):
        count += 1

print(count)
