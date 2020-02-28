def inttobinary(n):
    print('Entered number in binary: ')
    binaryNum = [0] * n

    i = 0
    while n > 0:
        binaryNum[i] = n % 2
        n = int(n / 2)
        i += 1

    for j in range(i - 1, -1, -1):
        print(binaryNum[j], end="")


n = int(input('Enter an integer: '))
inttobinary(n)
