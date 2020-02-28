size = int(input('Enter total number of elements in list: '))
list1, evenList, oddList = [], [], []
for j in range(0, size):
    num = int(input('Enter element of position {} '.format(j+1)))
    list1.append(num)

for num in list1:
    if num % 2 == 0:
        evenList.append(num)
    else:
        oddList.append(num)

print('List of even numbers:::: ', evenList)
print('List of odd numbers:::: ', oddList)
