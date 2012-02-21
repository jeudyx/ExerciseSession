'''
Exercises for session 1.
Jeudy Blanco - 02/21/2012
'''

import sys
import os

#This will be the program's entry point
def main(argv):
	
	path = argv[1]

	print "Hola. El path es: " + path
	for f in getFileNames(path) :
		print "File: " + f

def getFileNames(path):
	return os.listdir(path)

#---------------------------

main(sys.argv)
