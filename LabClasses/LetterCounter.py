__author__ = 'Vladislav'


class LetterCounter:
    def __init__(self, letter):
        self.letter = letter
        self.strings = []

    def enter_strings(self):
        print "Enter number of strings in text: ",
        number = input()
        for i in range(0, number):
            string = raw_input()
            self.strings.append(string)

    def count_occurrences(self):
        count = 0
        for string in self.strings:
            count += string.count(self.letter)
        return count
