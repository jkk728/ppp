n=int(input("숫자를 입력하시면 해당 숫자의 구구단을 출력해드립니다 : "))

dan=n
for n in range(1,10):
    print(f"{dan}x{n}={dan*n}")