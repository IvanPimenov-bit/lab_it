numbers=[1,4,56,7,66]
def calculate_sum(numbers):
    sm=0
    for n in numbers:
        sm+=n
    return sm
print(calculate_sum(numbers))
def find_min(numbers):
    mn=10**10
    for n in numbers:
        if n<mn:
            mn=n
    return mn
print(find_min(numbers))
def find_max(numbers):
    mx=0
    for n in numbers:
        if mx>n:
            n=mx

    return n
print(find_max(numbers))