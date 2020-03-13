ipAdd = input('Enter a valid IP address')
ipSplit1 = ipAdd.split('.')
ipSplit = []
for i in ipSplit1:
    ipSplit.append(int(i))

print('Next 4 IP addresses')
for i in range(4):
    if ipSplit[0] == ipSplit[1] == ipSplit[2] == ipSplit[3] == 255:
        print('No further IP address')
        break
    elif ipSplit[3] == 255 and ipSplit[2] == 255 and ipSplit[1] == 255:
        ipSplit[0] += 1
        ipSplit[3], ipSplit[2], ipSplit[1] = 0, 0, 0
    elif ipSplit[3] == 255 and ipSplit[2] == 255:
        ipSplit[1] += 1
        ipSplit[3], ipSplit[2] = 0, 0
    elif ipSplit[3] == 255:
        ipSplit[2] += 1
        ipSplit[3] = 0
    else:
        ipSplit[3] += 1
    print('{}.{}.{}.{}'.format(ipSplit[0], ipSplit[1], ipSplit[2], ipSplit[3]))
