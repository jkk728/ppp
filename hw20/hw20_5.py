import matplotlib.pyplot as plt
import pandas as pd
import koreanize_matplotlib

def main():
    plt.figure(figsize=(25, 6))

    year = [str(x + 1980) for x in range(45)]

    df_jj=pd.read_csv("weather_jeonju_1980-2024.csv",
                        skipinitialspace=True)
    df_sw=pd.read_csv("weather_suwon_1980-2024.csv",
                        skipinitialspace=True)

    Jeonju=[]
    Suwon=[]
    for y in range(1980, 2025):
        Jeonju.append(df_jj[df_jj["year"]==y]["tavg"].mean())
        Suwon.append(df_sw[df_sw["year"]==y]["tavg"].mean())

    plt.plot(year,Jeonju, color="r", label="전주시")
    plt.plot(year, Suwon, color="b", label="수원시")

    plt.ylabel("Temperature(℃)")
    plt.legend()
    plt.savefig("./hw20_5.png")

if __name__ == "__main__":
    main()
