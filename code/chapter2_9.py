from array import array
from random import random

floats = array('d', (random() for i in range(10**7)))
fin = open('fin.bin', 'wb')
floats.tofile(fin)
fin.close()
floats2 = array('d')
fout = open('fin.bin', 'rb')
floats2.fromfile(fout, 10**7)


"""
memoryview
"""


numbers = array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))
print(memv[0])
memv_oct = memv.cast('B')
print(memv_oct.tolist())
memv_oct[5] = 4
print(numbers)