inch = float(input("인치(inch)를 입력하세요: "))
cm = inch*2.54
print(f"{inch}인치는 {cm}cm입니다.")

kg = float(input("킬로그램(kg)을 입력하세요: "))
pound = kg * 2.20462
print(f"{kg}kg은 약 {pound:.2f}파운드입니다.")

import math
radius = float(input("원의 반지름을 입력하세요: "))
circumference = 2 * math.pi * radius
area = math.pi * (radius ** 2)
print(f"원의 둘레: {circumference:.2f}")
print(f"원의 넓이: {area:.2f}")
