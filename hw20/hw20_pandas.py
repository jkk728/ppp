import os
import requests
import pandas as pd

def download_weather(weather_filename, stid, sy,ey):
    url = f"https://api.taegon.kr/stations/{stid}/?sy={sy}&ey={ey}&format=csv"

    if not os.path.exists(weather_filename):
        resp = requests.get(url)
        print(resp.text)

        with open(weather_filename,"w") as fout:
            fout.write(resp.text)


def main():
    filename="weather_jeonju_1980-2024.csv"
    download_weather(filename,146,1980,2024)

    filename_sw = "weather_suwon_1980-2024.csv"
    download_weather(filename_sw, 119, 1980, 2024)

    df=pd.read_csv(filename, skipinitialspace=True)

    print("1) 전주시의 2012년 연 강수량: ", df[df["year"]==2012]["rainfall"].sum(),"mm")
    print("2) 전주시의 2024년 최대기온: ", df[df["year"] == 2024]["tavg"].max(),"ºC")
    df["tdiff"]=df["tmax"]-df["tmin"]
    print("3) 전주시의 2020년 최대 일교차:", df[df["year"] == 2020]["tdiff"].max(),"ºC")

    df_sw=pd.read_csv(filename_sw, skipinitialspace=True)

    prec_jj= df[df["year"]==2019]["rainfall"].sum()
    prec_sw= df_sw[df_sw["year"]==2019]["rainfall"].sum()
    print("4) 수원시와 전주시의 2019년 총강수량 차이: ", abs(prec_jj - prec_sw),"mm")


if __name__=="__main__":
    main()