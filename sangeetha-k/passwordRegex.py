import re
num1 = input('Enter a password')
found = re.match(r'(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}', num1)
if found:
    print('Strong Password')
else:
    print('Weak Password')
