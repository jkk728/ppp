import math

print(" 각(deg) |  라디안  |  sin  |  cos  |  tan  ")
print("-"*43)

for deg in range(0,11):
    r=math.radians(deg)
    s=math.sin(r)
    c=math.cos(r)
    t=math.tan(r)
    print(f"   {deg}º   | {r:.4f} | {s:.4f} | {c:.4f} | {t:.4f} ")