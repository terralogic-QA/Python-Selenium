size = int(input('Enter total number of elements in list: '))
list1 = []
for j in range(0, size):
    num = int(input('Enter element of position {} '.format(j+1)))
    list1.append(num)

total = 0
for num in list1:
    total = total + num
print('Sum of all elements in list is::: ', total)
