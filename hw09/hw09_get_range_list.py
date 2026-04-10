def get_range_list(n):
    nums=[]
    for i in range(1,n+1):
        nums.append(i)
    return nums

def main():
    n=int(input("아무 숫자나 입력하세요 : "))
    print(get_range_list(n))

if __name__=="__main__":
    main()