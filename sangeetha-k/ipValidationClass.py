ip = input('Enter an IP address')
try:
    parts = ip.split('.')
    if len(parts) == 4 and all(0 <= int(part) < 256 for part in parts):
        print('Valid IP address')
        if int(parts[0]) in range(0, 127):
            print('Class A')
        elif int(parts[0]) in range(128, 192):
            print('Class B')
        elif int(parts[0]) in range(192, 224):
            print('Class C')
        elif int(parts[0]) in range(224, 240):
            print('Class D')
        elif int(parts[0]) in range(240, 256):
            print('Class E')
        else:
            print('Loop back address')

    else:
        print('Ip address value is out of range or incomplete')
except ValueError:
    print('InValid IP address')
    # one of the 'parts' not convertible to integer
except (AttributeError, TypeError):
    print('InValid IP address - type')
    # ip isn't even a string