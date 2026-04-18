def read_text(filename):
    print(filename)
    with open(filename) as f:
        text=f.readline()
    return text

def text2list(nums):
    text=nums.split()
    nums_list=[]
    for t in text:
        nums_list.append(int(t))
    return nums_list

def main():
    text=read_text("numbers1.txt")
    text2list(text)

    nums=text2list(text)
    nums.sort()

    print(f"총 숫자의 개수는 {len(text2list(text))}개 입니다.")
    print(f"주어진 숫자의 평균은 {sum(text2list(text))/len(text2list(text))}입니다.")
    print(f"주어진 숫자의 최댓값은 {max(text2list(text))}입니다.")
    print(f"주어진 숫자의 최솟값은 {min(text2list(text))}입니다.")
    print(f"주어진 숫자의 중앙값은 {nums[len(nums)//2]}입니다.")

if __name__=="__main__":
    main()