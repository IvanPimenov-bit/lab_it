def calculate_rectangle(width, height):
    return width * height

def calculate_perimeter(width, height):
    return 2 * (width + height)

def describe_rectangle(width, height, unit="см"):
    print(f"Ширина: {width} {unit}, Высота: {height} {unit}")
    print(f"Площадь: {calculate_rectangle(width, height)} {unit}²")
    print(f"Периметр: {calculate_perimeter(width, height)} {unit}")

describe_rectangle(5, 10)
describe_rectangle(5, 10, "м")