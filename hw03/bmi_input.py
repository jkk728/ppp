import math
weight=float(input("몸무게(kg)를 입력하시오 : "))
height=float(input("키(cm)를 입력하시오 : "))

height_m=height/100
BMI=weight/(height_m**2)

print(f"BMI: {BMI}")