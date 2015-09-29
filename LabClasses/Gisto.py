import sys

__author__ = 'Vladislav'

class Gisto:
    def __init__(self, a, b):
        self._a = a.upper()
        self._b = b.upper()
        self.countA = 0
        self.countB = 0

    def plot(self):
        self.__readSeq()
        self.__plotChart()

    def __readSeq(self):
        print "Enter sequence (Escape - 0)"
        while True:
            c = raw_input()
            if c == '0':
                break
            if c.upper() == self._a:
                self.countA+=1
            if c.upper() == self._b:
                self.countB+=1


    def __plotChart(self):
        print "Chart:"
        print self._a, ": ",
        for i in range(0, self.countA): sys.stdout.write('*')
        print ''
        print  self._b, ": ",
        for i in range(0, self.countB): sys.stdout.write('*')


