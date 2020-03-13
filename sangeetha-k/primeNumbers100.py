print("Prime numbers between 0 and 100 are:")
count = 0
for num in range(0, 100 + 1):
    if num > 1:
        for i in range(2, num//2):
            if num % i == 0:
                break
        else:
            count = count+1
            print(num)

print('Total number of prime numbers between 0 and 100 are:::: ', count)
