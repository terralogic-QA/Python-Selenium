import re
num1 = input('Enter a number')
# found = re.match(r'([25][0-5]|[01]?[0-9][0-9]?|[2][0-4][0-9]([.]|$)){4}', num1)
found = re.match(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', num1)
if found:
    print('Valid IP Address')
else:
    print('Invalid IP Address')
