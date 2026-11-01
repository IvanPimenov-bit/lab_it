numbers=[-10,3,-2,8,-5]
print("обычная сортировка:",sorted(numbers))
print("по абс значению:",sorted(numbers, key=lambda x: abs(x)))