import random

print("구구단 10문제를 푸시오.")

def gugudan_correct():
    a= random.randint(2,9)
    b= random.randint(1,9)
    ans = input(f"{a} x {b} =>> ?")
    return int(ans) == a*b

def main():
    score=0
    for i in range(10):
        if gugudan_correct():
            score += 50
    print(f"500점 만점 중 {score}점입니다.")

if __name__=="__main__":
    main()