routerInfo = {"name": "Router1", "IP": "1.1.1.1", "username": "zframez", "pwd": "zframez"}
keyVal = input('Enter key name(name, IP, username, pwd) whose value need to be displayed: ')
if keyVal in routerInfo:
    print('Associated value of key is: ', routerInfo[keyVal])
else:
    print('Entered key is not found,')
    valueForKey = input('Please enter a value for the key')
    routerInfo.__setitem__(keyVal, valueForKey)

print(routerInfo)
