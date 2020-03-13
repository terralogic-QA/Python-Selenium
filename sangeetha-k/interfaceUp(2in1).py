import re

upCount = 0
upInterface = []
instr = "Interface ethernet0 is up\nInterface ethernet1 is down\nInterface serial0 is down\nInterface serial1 is up\n"
str1 = instr.split('\n')
for i in range(len(str1)):
    match = re.search(r'\bup\b', str1[i])
    if match:
        upCount += 1
        str3 = str1[i].split(' ')
        upInterface.append(str3[1])

print('Total number of interfaces that are up: ', upCount)
print('Interfaces that are up: ', upInterface)

