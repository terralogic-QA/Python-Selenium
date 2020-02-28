string1 = "Biryani is no compromise under any circumstance!"
res = []
for j, i in enumerate(string1):
    if j % 2 == 0:
        res.append(i.upper())
    else:
        res.append(i)

print(res)
