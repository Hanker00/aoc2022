with open("day2\day2.txt") as f:
    lines = f.read()
    lines = lines.split("\n")
    score_dict = {"X": 1, "Y": 2, "Z": 3}
    score_dict_2 = {"A": 1, "B": 2, "C": 3}
    total_score = 0
    for i in lines:
        if(i[2] == "Y"):
            total_score += (3 + score_dict_2[i[0]])
        elif(i[2] == "X"):
            if(i[0] == "A"):
                total_score += (score_dict["Z"])
            if(i[0] == "B"):
                total_score += (score_dict["X"])
            if(i[0] == "C"):
                total_score += (score_dict["Y"])
        elif(i[2] == "Z"):
            if(i[0] == "A"):
                total_score += (6 + score_dict["Y"])
            if(i[0] == "B"):
                total_score += (6 + score_dict["Z"])
            if(i[0] == "C"):
                total_score += (6 + score_dict["X"])
        print(total_score)
    print(total_score)