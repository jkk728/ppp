import math
weight=float(input("몸무게(kg)를 입력하시오 : "))
height=float(input("키(cm)를 입력하시오 : "))

height_m=height/100
BMI=weight/math.pow(height_m,2)

if 23<BMI<24.9:
    print("비만 전단계입니다.")
elif 25<BMI<29.9:
    print("1단계 비만입니다.")
elif 30<BMI<34.9:
    print("2단계 비만입니다.")
elif 35<=BMI:
    print("3단계 비만입니다.")

print(f"BMI: {BMI}")