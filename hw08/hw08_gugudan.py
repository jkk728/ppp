def gugudan(dan):
    for n in range(1, 10):
        print(f"{dan}x{n}={dan * n}")

def main():
    dan=int(input("몇 단을 출력할까요? : "))
    gugudan(dan)

if __name__=="__main__":
    main()