from LabClasses.FLParser import FLParser
from LabClasses.LetterCounter import LetterCounter
from LabClasses.RandSeq import RandSeq

__author__ = 'Vladislav'

# Tasks for Lab works 2
# 1 object - 1 task

#Task 4
parser = FLParser('b')
parser.do_task()

#Task 5
counter = LetterCounter('b')
counter.enter_strings()
print "Number of letters: ", counter.count_occurrences()

#Task 6
randSeq = RandSeq()
randSeq.do_task()