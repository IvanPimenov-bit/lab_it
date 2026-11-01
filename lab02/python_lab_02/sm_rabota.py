n=int(input("Введите кол-во измерений:"))
a=0
for i in range(n):
    i=float(input("Введите число:"))
    a+=i
print("Сумма:",a, "Среднее арифметическое",a/n)