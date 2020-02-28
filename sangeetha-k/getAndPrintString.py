class stringMethods:
    def get_String(self):
        getString = input('Enter a string:')
        print('String read: ', getString)

    def print_String(self, stri):
        print('String in uppercase:')
        print(stri.upper())


stringMethods.get_String(1)
stringMethods.print_String(1, "Hello World")