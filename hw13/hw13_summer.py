def read_weather_col(weather_filename, col_idx, conv_fn):
    dataset = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(conv_fn(tokens[col_idx]))
    return dataset

def sumifs(rainfalls, months, selected_months):
    total_value=0
    for i in range(len(rainfalls)):
        r=rainfalls[i]
        m=months[i]
        if m in selected_months:
            total_value += r
    return total_value

def main():
    weather_filename = "weather(146)_2022-2022.csv"

    rainfalls = read_weather_col(weather_filename, 9, float)
    months= read_weather_col(weather_filename, 1, int)

    summer_rainfall = sumifs(rainfalls, months, [6, 7, 8])
    print(f"여름철 강수량은 {summer_rainfall:.1f}mm입니다.")

if __name__ == "__main__":
    main()