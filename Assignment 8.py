import math

def calculate_area(shape, *values):
    if shape == "circle":
        return math.pi * values[0] * values[0]
    elif shape == "rectangle":
        return values[0] * values[1]
    elif shape == "triangle":
        return 0.5 * values[0] * values[1]

shape = input("Enter shape (circle/rectangle/triangle): ").lower()

if shape == "circle":
    radius = float(input("Enter radius: "))
    area = calculate_area(shape, radius)

elif shape == "rectangle":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = calculate_area(shape, length, width)

elif shape == "triangle":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = calculate_area(shape, base, height)

else:
    print("Invalid shape")
    exit()

print("Area =", area)