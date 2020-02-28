def fact(number):
    if number == 0:
        return 1
    elif number == 1:
        return 1
    else:
        return number * fact(number-1)


num = int(input('Enter a number'))
factorial = fact(num)
print('Factorial of {} is {}'.format(num, factorial))
