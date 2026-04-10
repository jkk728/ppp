def is_leap_year(y):
    if y%4==0 and y%100!=0:
        return True
    else:
        return False

def main():
    y=int(input("년도를 입력하세요 : "))
    if is_leap_year(y):
        print("윤년입니다. (True)")
    else:
        print("윤년이 아닙니다. (False)")

if __name__=="__main__":
    main()