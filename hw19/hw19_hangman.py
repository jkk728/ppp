import random

words=["spring","summer","fall","winter"]


def blank(answer):
    result=[]
    for i in answer:
        result.append("_")
    return result


def hangman():
    answer= random.choice(words)
    result= blank(answer)

    trial=7

    while trial>0 and "_" in result:
        print(" ".join(result))
        print(f"(trial={trial})")

        alphabet=input("답을 입력하세요 => ")

        if alphabet==answer:
            result=list(answer)

        elif alphabet in answer:
            for i in range(len(answer)):
                if answer[i]==alphabet:
                    result[i]=alphabet
        else:
            print("틀렸습니다.")
            trial=trial-1

    if "_" not in result:
        print("정답입니다.")
    else:
        print("게임 종료")


def main():
    hangman()


if __name__=="__main__":
    main()