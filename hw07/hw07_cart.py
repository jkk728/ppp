mart={"우유":2800, "계란":300, "빵":1200, "물":1700}

cart=["우유","계란","계란","계란","빵","물","물"]

total_cost=0
for item in cart:
    total_cost += mart[item]
    print(total_cost)
print(f"장바구니에 담은 품목의 가격은 총 {total_cost}원 입니다.")