#task 1
class str:
    def __init__(self):
        self.str = ""

    def getString(self):
        self.str = input()

    def printString(self):
        print(self.str.upper())

s = str()
s.getString()
s.printString()

