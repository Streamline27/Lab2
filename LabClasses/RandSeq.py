from random import randint

__author__ = 'Vladislav'


class RandSeq:
    def __init__(self):
        self.seq = []

    def do_task(self):
        self.__generate()
        self.__print()

    def __generate(self):
        for i in range(0, 40):
            self.seq.append(randint(1, 45))

    def __print(self):
        print "Direct order:",
        for i in self.seq:
            print i,
        print ""

        print "Reverse order",
        for i in reversed(self.seq):
            print i,
        print ""
