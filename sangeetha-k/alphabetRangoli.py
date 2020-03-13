import string

N = int(input('Enter a number'))
if N > 26:
    print('Number must be between 1 and 26')
else:
    mid = N - 1

    for i in range(N - 1, 0, -1):
        row = ['-'] * (2 * N - 1)
        for j in range(N - i):
            row[mid - j] = row[mid + j] = string.ascii_lowercase[j + i]
        print('-'.join(row))

    for i in range(0, N):
        row = ['-'] * (2 * N - 1)
        for j in range(N - i):
            row[mid - j] = row[mid + j] = string.ascii_lowercase[j + i]
        print('-'.join(row))