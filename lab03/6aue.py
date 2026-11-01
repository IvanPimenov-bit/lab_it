measurements = (10, 20, 30, 40, 50, 60, 70, 80)
print("Первый:", measurements[:1])
print("Последний:", measurements[-1:])
print("Срез:", measurements[2:5])
print("Кортежи неизменяемы, поэтому прямое изменение элемента вызывает ошибку")
first, second = measurements[0], measurements[1]
print(f"Первое: {first}, Второе: {second}")
temp_list = list(measurements)
temp_list[0] = 99
measurements = tuple(temp_list)
print("Изменённый кортеж:", measurements)
print(measurements[2:6])