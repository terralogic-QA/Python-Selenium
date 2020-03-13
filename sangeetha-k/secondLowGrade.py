studentList = []
newList = []

noOfStudents = int(input('Enter number of students'))
for i in range(noOfStudents):
    studentName = input('Enter name of student {} '.format(i+1))
    grade = int(input('Enter grade of student {} '.format(i+1)))
    studentList.append([studentName, grade])

print(studentList)

lowest = studentList[0][1]
secondLowest = studentList[1][1]
for i in range(1, len(studentList)-1):
    if studentList[i][1] < lowest:
        secondLowest = lowest
        lowest = studentList[i][1]
    elif studentList[i][1] < secondLowest:
        secondLowest = studentList[i][1]

print('Second lowest grade is: ', secondLowest)

for i in range(len(studentList)):
    if secondLowest in studentList[i]:
        newList.append(studentList[i][0])
print('Students with second lowest grade: ')
for element in sorted(newList):
    print(element, end='\n')





