def sum_n(n):
    total = 0
    for n in range(0, n + 1):
        total += n
    return total

def main():
    n=int(input("아무 숫자나 입력하시면 1부터 그 수까지 다 합해드립니다 : "))
    print(sum_n(n))

if __name__=="__main__":
    main()