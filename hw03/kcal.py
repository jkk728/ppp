h=float(input("한라봉 섭취 g를 입력하시오 : "))
s=float(input("딸기(설향) 섭취 g를 입력하시오 : "))
b=float(input("바나나 섭취 g를 입력하시오 : "))

h_kcal=h/100*50
s_kcal=s/100*34
b_kcal=b/100*77

print(f"한라봉 섭취 칼로리: {h_kcal}, 딸기(설향) 섭취 칼로리: {s_kcal}, 바나나 섭취 칼로리: {b_kcal}")

