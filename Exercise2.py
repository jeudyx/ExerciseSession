'''
Exercises for session 2.
Jeudy Blanco - 02/22/2012
'''

import sys
import os
import numpy
import inputdata

#Part 1: Create a NumPy array with the recommendations
class RecommendationsHolder(object):
	#Class constructor	
	def __init__(self, inputdatadicc):
		self.Persons = inputdatadicc.keys()
		self.Papers = set()			#Initially, the set of paper names is empty, will add them one by one

		#Adds the paper names into a set to ensure they are unique		
		for entry in inputdatadicc.values():
			for paper_name in entry.keys():
				self.Papers.add(paper_name)

		#Now that I have all the persons and the papers, I know how big the numpy array as to be

		self.Ratings = numpy.ndarray( (len(self.Persons), len(self.Papers)), dtype=float) 
		
		self.Ratings[:] = 0.
		
		#Now I can store the ratings
		i = 0		
		while(i < len(self.Persons)):
			j = 0			
			while(j < len(self.Papers)):
				
				if inputdatadicc[self.Persons[i]].has_key(list(self.Papers)[j]):
					 self.Ratings[i,j] = inputdatadicc[self.Persons[i]][list(self.Papers)[j]]
				else:
					self.Ratings[i,j] = 0.
				j = j + 1
			
			i = i + 1
#--------------------
def main(data):
	holder = RecommendationsHolder(data)
	#holder.PrintPapers()
	#print '-----------------'
	#print holder.Persons[2]	
	print holder.Ratings

main(inputdata.raw_scores)
