with open("day1\day1.txt") as f:
    lines = f.readlines()
    total_cal_list = []
    current_total = 0
    for i in lines:
        if i == '\n':
            total_cal_list.append(current_total)
            current_total = 0
        else:
            current_total += int((i.strip("\n")))
    value1 = max(total_cal_list)
    total_cal_list.remove(value1)
    value2 = max(total_cal_list)
    total_cal_list.remove(value2)
    value3 = max(total_cal_list)
    print(value1 + value2 + value3)