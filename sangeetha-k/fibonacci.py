def fib(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)


print('First 10 fibonacci numbers are:::')
for i in range(1, 11):
    print(fib(i))
