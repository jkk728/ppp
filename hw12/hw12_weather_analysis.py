def read_weather_col(filename, col_idx):
    dataset = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[col_idx]))
    return dataset


def read_rainfall(filename):
    dataset = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[9]))
    return dataset


def read_tmax(filename):
    dataset = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[3]))
    return dataset


def get_rain_event_days(rainfall):
    dataset_rainfall = []
    for m in rainfall:
        if m > 0:
            dataset_rainfall.append(1)
        else:
            dataset_rainfall.append(0)

    dataset_rain_event = []
    for i in range(len(dataset_rainfall)):
        m = dataset_rainfall[i]
        if m == 0:
            dataset_rain_event.append(0)

        else:
            if i == 0:
                dataset_rain_event.append(1)
            else:
                dataset_rain_event.append(dataset_rain_event[i - 1] + 1)
    return max(dataset_rain_event)


def get_rain_event_days(rainfall):
    datasets = []
    rainfall_event = []
    for r in rainfall:
        if r > 0:
            if rainfall_event != None:
                rainfall_event.append(r)
            else:
                rainfall_event = [r]
        else:
            if rainfall_event != None:
                datasets.append(rainfall_event)
            rainfall_event = None
    return max([sum(x) for x in datasets])


def get_top3(list_values):
    return sorted(list_values)[-3:]


def main():
    weather_filename = "weather(146)_2022-2022.csv"
    rainfall = read_weather_col(weather_filename, 9)

    max_rainy_days = get_rain_event_days(rainfall)
    print(f" 최장 연속 강우일수는 {max_rainy_days}일 입니다.")

    max_rainfall_event = get_rain_event_days(rainfall)
    print(f" 최대 강우량은 {max_rainfall_event}mm 입니다.")

    tmax = read_weather_col(weather_filename, 3)

    tmax_top3 = get_top3(tmax)
    print(f" tmax 최대값 3개는 {tmax_top3} 입니다.")


if __name__ == "__main__":
    main()