def analyze(numbers):
    minimum = numbers[0]
    maximum = numbers[0]
    total = 0
    for n in numbers:
        if n < minimum:
            minimum = n
        if n > maximum:
            maximum = n
        total += n
    average = total / len(numbers)
    return (minimum, maximum, average)

numbers = [5, 2, 8, 1, 9, 3, 7]
min_val, max_val, avg_val = analyze(numbers)
print(f"Минимум: {min_val}, Максимум: {max_val}, Среднее: {avg_val}")