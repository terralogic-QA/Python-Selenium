import re
str1 = "Latest release Version 3.7(1), RELEASE SOFTWARE. System bootstrap version 5.2(1)"
matchFound = re.findall(r'(?<=\b[vV]ersion\s)\w+[.]\w+[(]\w+[)]', str1)
for i in matchFound:
    print('Version number: ', i)
