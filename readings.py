import sys
import numpy

#print('version'sys.version)
#print('sys.argv',sys.argv)

script = sys.argv [0]
option = sys.argv [1]
filename = sys.argv [2:] #colon adds ability to process a list.

def reading(filename):
	data = numpy.loadtxt(filename, delimiter=',')
	if option == '--mean':  
		value = data.mean(axis = 1)
	elif option == '--max':
		value = data.max (axis = 1)
	print(value)

for filename in filename:
	reading (filename)
		
	


