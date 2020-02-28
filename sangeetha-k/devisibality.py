num1 = int(input('Enter value num1: '))
num2 = int(input('Enter value num2: '))
num3 = int(input('Enter value num3: '))
count = 0
if num1 < num2:
    for i in range(num1, num2+1):
        if i % num3 == 0:
            print(i, 'is divisible by', num3)
            count +=1
else:
    print('num1 must be less than num2')
