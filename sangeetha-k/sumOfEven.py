print('Sum of all even numbers from 0 to 10:::')
res = 0
for i in range(0, 11):
    if i % 2 == 0:
        res = res + i
print(res)
