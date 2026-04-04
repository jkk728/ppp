cal_dict={"한라봉":50,"딸기":34,"바나나":77, "사과":60, "배":55}

eat_dict={"한라봉":150, "딸기":50,"바나나":200, "사과":100, "배":110}

total_cal=0
for key, val in eat_dict.items():
    if key in cal_dict:
        total_cal+=val*cal_dict[key]
        print(total_cal)
print(f"한라봉, 딸기, 바나나, 사과, 배의 섭취 칼로리는 총 {total_cal}kcal 입니다.")