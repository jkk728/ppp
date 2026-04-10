def average(nums):
    average=sum(nums)/len(nums)
    return average

def main():
    text="6, 7, 2, 8"
    tokens=text.split(",")
    numbers=[]
    for token in tokens:
        numbers.append(int(token))
    print (average(numbers))

if __name__=="__main__":
    main()