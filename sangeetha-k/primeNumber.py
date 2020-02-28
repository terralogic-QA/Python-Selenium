num = int(input('Enter a number::: '))

# If given number is greater than 1
if num > 1:

    # Iterate from 2 to n / 2
    for i in range(2, num // 2):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

else:
    print(num, "is not a prime number")
