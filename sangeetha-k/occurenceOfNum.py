size = int(input('Enter total number of elements in list: '))
list1 = []
for j in range(0, size):
    num = int(input('Enter element of position {} '.format(j+1)))
    list1.append(num)
someNum = int(input('Enter the number to find frequency of occurrence'))

numCount = 0
for item in list1:
    if item == someNum:
        numCount += 1
print('Number {} appeared {} times in the list'.format(someNum, numCount))
