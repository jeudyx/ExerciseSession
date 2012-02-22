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
		for entry in inputdatadicc.values():
			for paper_name in entry.keys():
				self.Papers.add(paper_name)

	def PrintPersons(self):
		print self.Persons

	def PrintPapers(self):
		print self.Papers

#--------------------
def main(data):
	holder = RecommendationsHolder(data)
	holder.PrintPapers()
	#print '-----------------'
	#print holder.Persons[2]	
	

main(inputdata.raw_scores)
