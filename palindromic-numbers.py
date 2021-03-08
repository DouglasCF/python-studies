firstNumber = int(input('Type first number: '))
secondNumber = int(input('Type second number: '))

for i in range(firstNumber, secondNumber + 1):
    reversed = int(str(i)[::-1])
    if i == reversed:
        print(i)
