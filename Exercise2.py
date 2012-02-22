'''
Exercises for session 2.
Jeudy Blanco - 02/22/2012
'''

import sys
import os
import numpy
import inputdata


class RecommendationsHolder(object):
	#Class constructor	
	def __init__(self, inputdatadicc):
		self.Persons = inputdatadicc.keys()
		self.Papers = set()			#Initially, the set of paper names is empty, will add them one by one

	def PrintPersons(self):
		print self.Persons


#--------------------
def main(data):
	holder = RecommendationsHolder(data)
	#holder.PrintPersons()
	#print '-----------------'
	#print holder.Persons[2]	
	
	print data.values()[0].keys()

main(inputdata.raw_scores)
