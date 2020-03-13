found = 0
# first list
size = int(input('Enter total number of elements in list 1: '))
list1 = []
for j in range(0, size):
    num = int(input('Enter element of position {} '.format(j+1)))
    list1.append(num)
# second list
size1 = int(input('Enter total number of elements in list 2: '))
list2 = []
for j in range(0, size1):
    num = int(input('Enter element of position {} '.format(j+1)))
    list2.append(num)

for num in list1:
    if num in list2:
        found = 1
        print(num, 'is common in two lists')

if found == 0:
    print('There are no common elements in the list')
