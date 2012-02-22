'''
Exercises for session 2.
Jeudy Blanco - 02/22/2012
'''

import sys
import os
import numpy
import inputdata
import scipy
from scipy import stats

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
				#if the person hasn't read the paper, we assign a 0 as rate
				if inputdatadicc[self.Persons[i]].has_key(list(self.Papers)[j]):
					 self.Ratings[i,j] = inputdatadicc[self.Persons[i]][list(self.Papers)[j]]
				else:
					self.Ratings[i,j] = 0.
				j = j + 1
			
			i = i + 1
	
	def _getnonzeroelements(self, person1, person2):
		rate1 = self.Ratings[person1]
		rate2 = self.Ratings[person2]
		
		comp = []

		i = 0

		while(i < len(rate1)):
			if rate1[i] > 0 and rate2[i]:
				comp.append(True)
			else:
				comp.append(False)
		
			i = i + 1

		#print comp
		
		clean_rate1 = []
		clean_rate2 = []

		i = 0
		for val in comp:
			if val:
				clean_rate1.append(rate1[i])
				clean_rate2.append(rate2[i])
			i = i + 1

		if len(clean_rate1) == 0 and len(clean_rate2) == 0:
			return None
		else:
			return [clean_rate1,clean_rate2]
		
	def Rates2Norm(self, person1, person2):
		clean_rates = self._getnonzeroelements(person1, person2)		
		if clean_rates == None:
			return 0.
		else:
			return numpy.linalg.norm(clean_rates)

	def RatesPearson(self, person1, person2):
		clean_rates = self._getnonzeroelements(person1, person2)
		return scipy.stats.pearsonr(clean_rates[0], clean_rates[1])

#		print rate2
#--------------------
def main(data):
	holder = RecommendationsHolder(data)
	#holder.PrintPapers()
	#print '-----------------'
	#print holder.Persons[2]
	print holder.Persons
	print '-----------------'
	print holder.Papers
	print '-----------------'	
	print holder.Ratings
	print '-----------------'	
	print 'Norma: ' + str(holder.Rates2Norm(0,1))
	#print 'Pearson: ' + str(holder.RatesPearson(0,1))
	
main(inputdata.raw_scores)
