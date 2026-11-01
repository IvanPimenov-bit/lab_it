number=int(input("Введите целое число:"))
if number>0:
    print("Число положительное")
elif number<0:
    print("Число отрицательное") 
else:
    print("Число равно нулю,четное")
if abs(number)%2==0:
    print("Число четное")
else:
    print("Число нечетное")