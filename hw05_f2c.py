x=input("변환할 단위를 입력하시오 (섭씨/화씨/피트/센티미터 중 선택) : ")

if x=="섭씨":
    temp_c=float(input("섭씨 온도를 입력하시오 : "))
    temp_f=temp_c*1.8+32
    print(f"{temp_c}℃ => {temp_f:.1f}℉")

elif x=="화씨":
    temp_f=float(input("화씨 온도를 입력하시오 : "))
    temp_c=(temp_f-32)*5/9
    print(f"{temp_f}℉ => {temp_c:.1f}℃")

elif x=="피트":
    ft=float(input("피트(ft)를 입력하시오 : "))
    cm=ft*30.48
    print(f"{ft}ft => {cm:.1f}cm")

elif x=="센티미터":
    cm=float(input("센티미터(cm)를 입력하시오 : "))
    ft=cm/30.48
    print(f"{cm}ft => {ft:.1f}cm")