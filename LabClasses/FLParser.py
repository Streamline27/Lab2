__author__ = 'Vladislav'


class FLParser:
    def __init__(self, symbol):
        self.strings = []
        self.symbol = symbol

    def do_task(self):
        self.__enter_strings()
        self.__print()

    def __enter_strings(self):
        print "Enter number of strings: ",
        number = input()
        for i in range(0, number):
            string = raw_input()
            self.strings.append(string)

    def __print(self):
        for string in self.strings:
            if string[0] == self.symbol:
                print string