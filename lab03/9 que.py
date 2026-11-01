def find_element(number,target):
    for i in range(len(number)):
        if number[i]==target:
            return i
    return -1
numbers=[1,123,4,45,2,56]
print("Индекс 4:",find_element(numbers,4))
print("Индекс 7:",find_element(numbers,7))