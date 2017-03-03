import numpy

n=numpy.arange(27)
print(n)
n = n.reshape(3,9)
print(n)
n = n.reshape(3,3,3)
print(n)

m=numpy.asarray([[123,12,123,12,33],[],[]]) #converts to real numpy array
print(m)
