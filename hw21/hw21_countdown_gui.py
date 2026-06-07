import PySimpleGUI as sg
import time

def main():
    layout = [
        [sg.Text("카운트다운을 시작할까요?")],
        [sg.Button("OK"), sg.Button("Cancel")]]

    window = sg.Window("Test", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cancel":
            break
        if event == "OK":
            for i in range(10, 0, -1):
                print(f"{i:3d}")
                time.sleep(1)
            print("시간이 종료되었습니다.")
    window.close()

if __name__ == "__main__":
    main()