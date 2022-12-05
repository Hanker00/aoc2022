with open("day2\day2.txt") as f:
    lines = f.read()
    lines = lines.split("\n")
    score_dict = {"X": 1, "Y": 2, "Z": 3}
    total_score = 0
    for i in lines:
        print(i[0] + i[2])
        if((ord(i[0]) - ord(i[2])) == -23):
            total_score += (3 + score_dict[i[2]])
        elif(i[0] == "A" and i[2] == "Y"):
            total_score += (6 + score_dict[i[2]])
        elif(i[0] == "B" and i[2] == "Z"):
            total_score += (6 + score_dict[i[2]])
        elif(i[0] == "C" and i[2] == "X"):
            total_score += (6 + score_dict[i[2]])
        else:
            total_score += score_dict[i[2]]
        print(total_score)
    print(total_score)
            