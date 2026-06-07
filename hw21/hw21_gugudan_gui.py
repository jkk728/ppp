import random
import PySimpleGUI as sg

def gugudan_correct():
    a = random.randint(2, 9)
    b = random.randint(1, 9)

    layout = [
        [sg.Text(f"{a} x {b} = ?")],
        [sg.Input(key='-ANS-')],
        [sg.Button("OK"), sg.Button("Exit")]]

    window = sg.Window("구구단 10문제를 푸시오.", layout)

    event, values = window.read()
    window.close()

    if event == sg.WIN_CLOSED or event == "Exit":
        return False
    try:
        return int(values['-ANS-']) == a * b
    except:
        return False


def main():
    sg.popup("구구단 10문제를 푸시오.")

    score = 0
    for i in range(10):
        if gugudan_correct():
            score += 50

    sg.popup(f"500점 만점 중 {score}점입니다.")

if __name__ == "__main__":
    main()