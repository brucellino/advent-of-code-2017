import numpy as np

data = np.recfromtxt('input2.txt')
checksum=0
for row in data:
    checksum += (row.max() - row.min())

print "checksum is %d" % checksum

