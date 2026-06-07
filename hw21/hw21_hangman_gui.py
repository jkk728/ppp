import random
import tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
root.withdraw()

words = ["spring", "summer", "fall", "winter"]

def blank(answer):
    result = []
    for i in answer:
        result.append("_")
    return result

def hangman():
    answer = random.choice(words)
    result = blank(answer)

    trial = 7

    while trial > 0 and "_" in result:
        print(" ".join(result))
        print(f"(trial={trial})")

        alphabet = simpledialog.askstring(title="Hangman", prompt="출력값을 보면서 답을 입력하세요 =>")

        if alphabet is None:
            break

        if alphabet == answer:
            result = list(answer)

        elif alphabet in answer:
            for i in range(len(answer)):
                if answer[i] == alphabet:
                    result[i] = alphabet
        else:
            print("틀렸습니다.")
            trial -= 1

    if "_" not in result:
        print("정답입니다.")
    else:
        print("게임 종료")


def main():
    hangman()


if __name__ == "__main__":
    main()