num1 = int(input('Enter value num1: '))
num2 = int(input('Enter value num2: '))
num3 = int(input('Enter value num3: '))
if num1 < num2 and num1 < num3:
    print('smallest num is {}'.format(num1))
elif num2 < num3:
    print('smallest num is {}'.format(num2))
else:
    print('smallest num is {}'.format(num3))
