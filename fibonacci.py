# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

def fibonacci(size):
    sequence = ''
    num1 = 0
    num2 = 1
    for _ in range(size + 1):
        sequence += str(num1) + ', '
        aux = num1 + num2
        num2 = num1
        num1 = aux
    print(sequence[:-2])


fibonacci(0)  # 0
fibonacci(1)  # 0, 1
fibonacci(2)  # 0, 1, 1
fibonacci(3)  # 0, 1, 1, 2
fibonacci(7)  # 0, 1, 1, 2, 3, 5, 8, 13
fibonacci(10)  # 0, 1, 1, 2, 3, 5, 8, 13, ..., 55
fibonacci(50)  # 0, 1, 1, 2, 3, 5, 8, 13, ..., 12586269025
