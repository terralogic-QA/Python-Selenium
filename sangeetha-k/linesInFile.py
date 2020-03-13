try :
    fname = "sample.txt"
    count = 0
    with open(fname, 'r') as f:
        for line in f:
            count += 1
    print("Total number of lines is:", count)
except IOError:
    print('No file found: Please provide valid file name/path')
