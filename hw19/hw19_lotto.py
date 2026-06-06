import random

def lotto():
    num = random.randint(1,45)
    return num


def main():
    count=int(input("원하는 횟수를 입력하시면 해당 횟수만큼 반복하여 로또 번호를 추출해드립니다: "))

    for i in range(count):
        result=[]
        while len(result)<6:
            num=lotto()
            if num not in result:
                result.append(num)
        print(result)


if __name__=="__main__":
    main()