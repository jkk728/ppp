def read_tavg(weather_filename):
    dataset=[]
    with open (weather_filename) as f:
        lines=f.readlines()
        for line in lines[1:]:
            tokens=line.split(",")
            dataset.append(float(tokens[4]))
    return dataset

def read_rainfall(weather_filename):
    dataset=[]
    with open (weather_filename) as f:
        lines=f.readlines()
        for line in lines[1:]:
            tokens=line.split(",")
            dataset.append(float(tokens[9]))
    return dataset

def read_over_five(rainfalls):
    count_5mm=0
    for r in rainfalls:
        if r>= 5:
            count_5mm+=1
    return count_5mm


def main():
    weather_filename = "weather(146)_2022-2022.csv"

    tavgs = read_tavg(weather_filename)
    print(f"연 평균 기온은 {sum(tavgs)/len(tavgs)}ºC입니다.")

    rainfalls = read_rainfall(weather_filename)
    print(f"총 강우량은 {sum(rainfalls)}mm입니다.")

    over_five = read_over_five(rainfalls)
    print(f"5mm 이상인 총 강우 일수는 {over_five}일 입니다.")

if __name__=="__main__":
    main()