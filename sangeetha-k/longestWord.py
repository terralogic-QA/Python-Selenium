longest = 0
string = "Biryani is no compromise under any circumstance!"
# Finding longest word in sentence
for word in string.split():
    if len(word) > longest:
        longest = len(word)

print('Length of longest word is', longest)
