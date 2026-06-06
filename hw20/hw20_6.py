import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

def main():
    fig, ax = plt.subplots(figsize=(25, 6))

    year = [str(x+1980) for x in range(45)]

    df=pd.read_csv("weather_jeonju_1980-2024.csv", skipinitialspace=True)

    rain = []
    for y in range(1980, 2025):
        rain.append(df[df["year"]==y]["rainfall"].sum())

    ax.bar(year, rain, color="b")
    ax.set_ylabel("전주시 연간 강수량(mm)")
    fig.savefig("./hw20_6.png")

if __name__ == "__main__":
    main()