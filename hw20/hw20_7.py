import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

def graph(birthday):
    plt.figure(figsize=(25, 6))

    year=[str(x + 1980) for x in range(45)]
    temp=birthday["tavg"]

    plt.plot(year, temp, color="r")
    plt.ylabel("연도별 7월 28일 평균 기온(℃)")
    plt.savefig("./hw20_7.png")


def main():
    df = pd.read_csv("weather_jeonju_1980-2024.csv", skipinitialspace=True)

    birthday = df[(df["month"] == 7) & (df["day"] == 28)]
    graph(birthday)

    temp_2006=birthday[birthday["year"] == 2006]["tavg"].max()

    rank = 1
    for i in birthday["tavg"]:
        if i > temp_2006:
            rank += 1
    print(f"2006년은 {rank}번째로 온도가 높았던 해입니다.")

    max_temp = birthday["tavg"].max()
    for i in birthday.index:
        if birthday["tavg"][i]==max_temp:
            print(f"가장 온도가 높았던 해: {birthday['year'][i]}년")

    min_temp = birthday["tavg"].min()
    for i in birthday.index:
        if birthday["tavg"][i]==min_temp:
            print(f"가장 온도가 낮았던 해: {birthday['year'][i]}년")


if __name__=="__main__":
    main()