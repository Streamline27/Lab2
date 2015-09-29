__author__ = 'Vladislav'

class SeqGen:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def generate(self):
        print "Sequence: "
        for i in range(1, 10):
            if i != self.x and i!=self.y : print i