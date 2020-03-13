import re
num1 = input('Enter a number')
found = re.match(r'[0-9]*[.][0-9]+', num1)
if found:
    print('Float')
else:
    print('Not float')
