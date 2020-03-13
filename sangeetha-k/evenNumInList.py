size = int(input('Enter total number of elements in list : '))
list1 = []
for j in range(0, size):
    num = int(input('Enter element of position {} '.format(j+1)))
    list1.append(num)

print('Even numbers in the list::: ')
for num in list1:
    if num % 2 == 0:
        print(num)
