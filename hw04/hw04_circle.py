import math

r=float(input("반지름을 입력하시오 : "))

A=math.pi*(r**2)
P=math.pi*(2*r)

print(f"원의 면적 : {A:.2f}")
print(f"원의 둘레 : {P:.1f}")
