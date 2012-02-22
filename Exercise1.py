'''
Exercises for session 1.
Jeudy Blanco - 02/21/2012
'''

import sys
import os


#This will be the program's entry point
def main(argv):
	
	path = argv[1]

	filelist = getFileNames(path)

	for filename in filelist:
		fixDataFile(path, filename)

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

'''
Fix a file that contains a negative response, replacing it with an M
Path must end in /
'''
def fixDataFile(path, filename):
	tempfile = open(path + filename + ".tmp", 'w')	
	filehandle = open(path + filename, 'r')

	rename_needed = False

	for line in filehandle:
		if containsNResponse(line):
			correct_line = line.replace(": N", ": M")
			print "Negative response found in file: " + path + filename + " -- response: " + line + " -- corrected: " + correct_line
			tempfile.write(correct_line)
			rename_needed = True
		else:
			tempfile.write(line)
	
	filehandle.close()
	tempfile.close()
#Need to rename the new file, and take a backup of the old one
	
	if rename_needed :
		os.rename(path + filename, path + filename + ".old")
		os.rename(path + filename + ".tmp", path + filename)
	else:
		os.remove(path + filename + ".tmp")

#----------------------------

main(sys.argv)
