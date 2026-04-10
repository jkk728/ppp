def kcal(cal_dict, eat_dict):
    total_cal = 0
    for key, val in eat_dict.items():
        if key in cal_dict:
            total_cal += val * cal_dict[key]
    return total_cal

def main():
    cal_dict = {"한라봉": 50, "딸기": 34, "바나나": 77}
    eat_dict = {"한라봉": 50, "딸기": 100, "바나나": 200}
    print(kcal(cal_dict, eat_dict))

if __name__=="__main__":
    main()