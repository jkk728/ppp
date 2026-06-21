import PySimpleGUI as sg
import telegram
import asyncio
import os
import math

token = '8730407189:AAFHuDk3Ck4PMb-azWM0x0YJN2wYXVynHRg'
chat_id = '8824215737'


def calc_vpd(temp, humid):
    svp = 0.6108 * math.exp((17.27 * temp) / (temp + 237.3))
    vpd = svp * (1 - humid / 100)
    return round(vpd, 2)


def check_env(temp, humid, co2):
    result= ""
    if 20 <= temp <= 28:
        result += "온도 : 적정\n"
    elif temp < 20:
        result += "온도 : 낮음\n"
    elif temp > 28:
        result += "온도 : 높음\n"

    if 65 <= humid <= 80:
        result += "습도 : 적정\n"
    elif humid < 65:
        result += "습도 : 낮음\n"
    elif humid > 80:
        result += "습도 : 높음\n"

    if 400 <= co2 <= 1000:
        result += "이산화탄소 농도 : 적정\n"
    elif co2 < 400:
        result += "이산화탄소 농도 : 낮음\n"
    elif co2 > 1000:
        result += "이산화탄소 농도 : 높음\n"


    if (20 <= temp <= 28 and
        65 <= humid <= 80 and
        400 <= co2 <= 1000):
        msg = "오늘의 온실 생육 환경은 적합합니다."
        result += "\n오늘의 온실 생육 환경은 적합합니다."
    else:
        msg = "오늘의 온실 생육 환경은 적합하지 않습니다.\n"
        if temp < 20:
            msg += "\n- 온도가 낮습니다."
        elif temp > 28:
            msg += "\n- 온도가 높습니다."

        if humid < 65:
            msg += "\n- 습도가 낮습니다."
        elif humid > 80:
            msg += "\n- 습도가 높습니다."

        if co2 < 400:
            msg += "\n- 이산화탄소 농도가 낮습니다."
        elif co2 > 1000:
            msg += "\n- 이산화탄소 농도가 높습니다."


    vpd = calc_vpd(temp, humid)

    if 0.54 <= vpd <= 1.28:
        result += f"\nVPD : {vpd} kPa (적정)\n"
    elif vpd < 0.54:
        result += f"\nVPD : {vpd} kPa (낮음)\n"
    elif vpd > 1.28:
        result += f"\nVPD : {vpd} kPa (높음)\n"

    if vpd < 0.54:
        msg += "\n- VPD가 낮습니다."
    elif vpd > 1.28:
        msg += "\n- VPD가 높습니다."

    return result, msg


async def send_msg(msg):
    bot = telegram.Bot(token=token)
    await bot.send_message(chat_id=chat_id, text=msg)


def save_data(year, month, day, temp, humid, co2):
    vpd = calc_vpd(float(temp), float(humid))
    if not os.path.exists("tomato.csv"):
        f = open("tomato.csv", "w")
        f.write("year, month, day, temp, humid, co2, vpd\n")
        f.close()

    f = open("tomato.csv", "a")
    f.write(f"{year}, {month}, {day}, {temp}, {humid}, {co2}, {vpd}\n")
    f.close()


def main():
    layout = [
        [sg.Text("전북대 토마토 생육 온실")],
        [sg.Text("년도"), sg.Input(key="-YEAR-", size=(10, 1))],
        [sg.Text("월"), sg.Input(key="-MONTH-", size=(10, 1))],
        [sg.Text("일"), sg.Input(key="-DAY-", size=(10, 1))],
        [sg.Text("온도 (ºC)"), sg.Input(key="-TEMP-",size=(10, 1))],
        [sg.Text("습도 (%)"), sg.Input(key="-HUMID-",size=(10, 1))],
        [sg.Text("이산화탄소 농도 (ppm)"), sg.Input(key="-CO2-",size=(10, 1))],
        [sg.Button("분석"),
         sg.Button("저장"),
         sg.Button("종료")],
        [sg.Multiline(size=(70,10), key="-RESULT-")]]
    window = sg.Window("토마토 맞춤형 온실 프로그램", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "종료":
            break

        if event == "분석":
            temp = float(values["-TEMP-"])
            humid = float(values["-HUMID-"])
            co2 = float(values["-CO2-"])
            result, msg = check_env(temp, humid, co2)
            window["-RESULT-"].update(result)
            asyncio.run(send_msg(msg))

        if event == "저장":
            save_data(values["-YEAR-"],values["-MONTH-"],values["-DAY-"],
                      values["-TEMP-"],values["-HUMID-"], values["-CO2-"])
            window["-RESULT-"].update("데이터가 저장되었습니다.")
    window.close()


if __name__=="__main__":
    main()