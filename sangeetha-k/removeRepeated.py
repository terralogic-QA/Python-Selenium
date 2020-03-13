size = int(input('Enter total number of elements in list: '))
list1, newList = [], []
for j in range(0, size):
    num = int(input('Enter element of position {} '.format(j+1)))
    list1.append(num)

for num in list1:
    if num not in newList:
        newList.append(num)
        
print('List after removing duplicates:::: ', newList)
