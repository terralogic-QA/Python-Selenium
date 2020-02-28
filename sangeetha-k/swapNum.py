num1 = int(input('Enter value num1: '))
num2 = int(input('Enter value num2: '))
print('Entered numbers are: num1 = {} and num2 = {}'.format(num1, num2))
temp = num1
num1 = num2
num2 = temp
print('Numbers after swapping: num1 = {} and num2 = {}'.format(num1, num2))
