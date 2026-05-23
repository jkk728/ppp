import requests
import os

def read_tavg(filename):
    dataset=[]
    with open (filename,encoding="utf-8") as f:
        lines=f.readlines()
        for line in lines[1:]:
            tokens=line.split(",")
            dataset.append(float(tokens[4]))
    return dataset

def read_rainfall(filename):
    dataset=[]
    with open (filename,encoding="utf-8") as f:
        lines=f.readlines()
        for line in lines[1:]:
            tokens=line.split(",")
            dataset.append(float(tokens[9]))
    return dataset


def read_over_five(rainfall):
    count_5mm=0
    for r in rainfall:
        if r>= 5:
            count_5mm+=1
    return count_5mm

def main():
    year=2023
    url=f"https://api.taegon.kr/stations/146/?sy={year}&ey={year}&format=csv"

    resp=requests.get(url)
    filename=f"weather_{year}.csv"

    if not os.path.exists(filename):
        resp = requests.get(url)
        print(resp.text)

        with open(filename,"w",encoding="utf-8") as fout:
            fout.write(resp.text)

    with open(filename, "w") as fout:
        fout.write(resp.text)

    tavg=read_tavg(filename)
    rainfall=read_rainfall(filename)
    over_five=read_over_five(rainfall)

    with open("result.txt","w",encoding="utf-8") as fout:
        fout.write(f"연 평균 기온: {sum(tavg)/len(tavg):.1f}도\n")
        fout.write(f"5mm 이상 강우일수: {over_five}일\n")
        fout.write(f"총 강우량 {sum(rainfall)}mm")

if __name__=="__main__":
    main()