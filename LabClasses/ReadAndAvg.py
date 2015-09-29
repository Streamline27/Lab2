__author__ = 'Vladislav'

class ReadAndAvg:
    def __int__(self):
        pass

    def do(self):
        sum = 0
        n = input("Number of numbers: ")
        for i in range(0, n):
            sum+=input("number: ")
        print "Average:", sum/n