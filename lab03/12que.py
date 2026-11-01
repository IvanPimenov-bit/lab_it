def calculate_average(measurements):
    sm=0
    for n in measurements:
        sm+=n
    return sm/len(measurements)
def find_minimum(measuremants):
    mn=10**10
    for n in measuremants:
        if n<mn:
            mn=n
    return mn
def find_maximum(measurements):
    mx=0
    for n in measurements:
        if n>mx:
            mx=n
    return mx
def count_above_average(measurements):
    avg=calculate_average(measurements)
    k=0
    for n in measurements:
        if n>avg:
            k+=1
    return k
def find_value(measurements,target):
    for i in range(len(measurements)):
        if measurements[i]==target:
            return i
    return -1
def analyze_measurements(measurements):
    return (find_minimum(measurements),find_maximum(measurements),calculate_average(measurements))
measurements=[12,3.4,12.4,32.3,6.7,5.4,10.3,11.3,8.55,15.4]
minimun, maximum, average=analyze_measurements(measurements)
print("Количество измерений:", len(measurements))
print("Минимальное значение:", find_minimum(measurements))
print("Максимальное значение:", find_maximum(measurements))
print("Среднее значение:", calculate_average(measurements))
print("Количество значений выше среднего:", count_above_average(measurements))

target = float(input("Введите значение для поиска: "))
result = find_value(measurements, target)
if result != -1:
    print("Значение найдено, индекс:", result)
else:
    print("Значение не найдено")