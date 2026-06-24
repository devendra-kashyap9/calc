# This is a program to add 2 Numbers

def add(a: float, b:float) -> float:
    return a + b

a, b = [float(x) for x in input('Enter two numbers to perform addition seperated by ",": ').split(',')]
sum = add(a, b)

print(f'The resultatnt sum of {a} & {b} is {sum}')
print(f"Multiplication: {a} * {b} = {a * b}")
