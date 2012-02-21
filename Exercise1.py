'''
Exercises for session 1.
Jeudy Blanco - 02/21/2012
'''

import sys
import os

#This will be the program's entry point
def main(argv):
	
	path = argv[1]

	print containsNResponse("CI type: 8")
	print containsNResponse("Sex: N")

	#print "Hola. El path es: " + path
	#for f in getFileNames(path) :
	#	print "File: " + f

#This function returns the content of a directory in a list
def getFileNames(path):
	return os.listdir(path)

'''
This function returns true if the provided line contains a 
negative response. Assumes upper case N separated 
by : and a white space after the question
'''
def containsNResponse(line):
	return line.find(": N") > 0
#---------------------------



main(sys.argv)
