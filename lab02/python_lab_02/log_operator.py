age=int(input("Напишите свой возраст:"))
has_access=input("Допуск к лабораторной работе:")=="да"
if age>17 and has_access:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")