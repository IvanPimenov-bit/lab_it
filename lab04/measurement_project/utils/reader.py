def read_numbers(path):
    with open(path,"r") as f:
        lines=f.readlines()
    numbers=[]
    for line in lines:
        numbers.append(float(line.strip()))
    return numbers
