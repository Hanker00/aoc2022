with open("day3/input.txt") as f:
    rucksacks = f.read().split("\n")

total_sum = 0
for rucksack in rucksacks:
    first, second = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
    for letter in first:
        if letter in second:
            if letter.isupper():   
                total_sum += (ord(letter) - 38)
            else:
                total_sum += (ord(letter) - 96)
            break

sum_two = 0
i = 0
while i < (len(rucksacks) - 2):
    print("i is ", i)
    for letter in rucksacks[i]:
        if letter in rucksacks[i + 1] and letter in rucksacks[i + 2]:
            if letter.isupper():
                sum_two += (ord(letter) - 38)
            else:
                sum_two += (ord(letter) - 96)
            break
    i += 3
print(sum_two)