import random
import PySimpleGUI as sg

def lotto():
    return random.randint(1, 45)


def main():
    layout = [
        [sg.Text("원하는 횟수를 입력하세요")],
        [sg.Input(key='-COUNT-')],
        [sg.Button("OK"), sg.Button("Cancel")]]

    window = sg.Window("로또 번호를 생성해드립니다.", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Cancel":
            break

        if event == "OK":
            count = int(values['-COUNT-'])
            for i in range(count):
                result = []
                while len(result) < 6:
                    num = lotto()
                    if num not in result:
                        result.append(num)
                print(result)
    window.close()


if __name__ == "__main__":
    main()