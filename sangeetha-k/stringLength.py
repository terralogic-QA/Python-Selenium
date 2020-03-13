def findLen(str):
    count = 0
    for i in str:
        count += 1
    return count


str = "Biryani is an evergreen classic that really needs no introduction"
print('Length of given string', findLen(str))
