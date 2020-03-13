monthDict = {1: 'January', 2: 'Febraury', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
date = input('Enter a date in dd-mm-yyyy format')
dateSplit = date.split('-')
monthNum = int(dateSplit[1])
if 0 < monthNum <= 12:
    monthName = monthDict[monthNum]
    print('Month is: ', monthName)
else:
    print('Enter a valid month')
