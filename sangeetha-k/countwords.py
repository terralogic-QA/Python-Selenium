import operator
try:
    text = open("sample.txt", "r")
    d = dict()
    for line in text:
        line = line.strip()
        line = line.lower()
        words = line.split(" ")
        for word in words:
            if word in d:
                # Increment count of word by 1
                d[word] = d[word] + 1
            else:
                # Add the word to dictionary with count 1
                d[word] = 1
    # Print the contents of dictionary
    # for key in d.keys():
    for key in dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True)):
        print('{} : {}'.format(key, d[key]))
except IOError:
    print('No file found: Please provide valid file name/path')
