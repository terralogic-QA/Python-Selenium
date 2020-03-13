num = int(input('Enter an integer: '))
if num == 0:
    print('Ignore! entered number is 0')
elif num % 2 == 0:
    print('Entered number is an even number')
    print('Square of given num :::', num*num)
else:
    print('Entered number is an odd number')
    print('Cube of given num :::', pow(num, 3))