def read_weather_col(weather_filename, col_idx=9, conv_fn=float):
    dataset = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(conv_fn(tokens[col_idx]))
    return dataset

def sumifs(rainfalls, years, selected_years):
    total_value=0
    for i in range(len(rainfalls)):
        r=rainfalls[i]
        y=years[i]
        if y in selected_years:
            total_value += r
    return total_value

def main():
    weather_filename = "weather(146)_2001-2022.csv"

    rainfalls = read_weather_col(weather_filename)
    years= read_weather_col(weather_filename, 0, int)

    for y in range(2001, 2023):
        rainfall_y= sumifs(rainfalls, years, [y])
        print(f"{y}년 강수량은 {rainfall_y:.1f}mm입니다.")

if __name__ == "__main__":
    main()