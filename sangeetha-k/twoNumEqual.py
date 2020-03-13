num1 = int(input('Enter value num1: '))
num2 = int(input('Enter value num2: '))
num3 = int(input('Enter value num3: '))
someNum = num1
if num1 == num2:
    print('num1 : {} and num2 : {} are same'.format(num1,num2))
elif num1 == num3:
    print('num1 : {} and num3 : {} are same'.format(num1, num3))
elif num2 == num3:
    print('num2 : {} and num3 : {} are same'.format(num2, num3))
else:
    print('No numbers are repeated')