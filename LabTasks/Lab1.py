from LabClasses.Gisto import Gisto
from LabClasses.ReadAndAvg import ReadAndAvg
from LabClasses.SeqGen import SeqGen

__author__ = 'Vladislav'

# Tasks for lab work 1
# 1 object - 1 task

#Task 1
seqGen = SeqGen(2, 5)
seqGen.generate()

#Task 2
readAndAvg = ReadAndAvg()
readAndAvg.do()

#Task 3
gisto = Gisto('a', 'b')
gisto.plot()