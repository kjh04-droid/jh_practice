import math
radius = float(input("원의 반지름을 입력하세요: "))
circumference = 2 * math.pi * radius
area = math.pi * (radius ** 2)
print(f"원의 둘레: {circumference:.2f}")
print(f"원의 넓이: {area:.2f}")
