import numpy as np
import random
from Patch import Patch


class Map:
	#Attributes

	__grid = np.empty((41,41), dtype= int)
	__patches = np.empty((41,41), dtype = Patch) #list of patches

	def __init__(self):
		#self.__grid = np.random.randint(10, size= (41,41))
		#self.__grid = np.ones((41,41))
		self.__lorenz_points = 0.0
		self.__gini_index_reserve = 0.0
		self.__avg_ambition = 0.0
		self.__avg_competency = 0.0


	def getPatches(self):
		return self.__patches

	def getGrid(self):
		return self.__grid


	def createPatches(self):
		#Use multiprocessing
		count = 0
		for r in range(41):
			for c in range(41):
				self.__patches[r,c] = Patch(count, True) #this should insert a Patch object - I made every Patch a Field
				count += 1
		return self.__patches

		#populate list of patches

	def getPatches(self):
		return self.__patches


	def createRiver(self):
		#change patches isRiver true
		#making first 2 columns river
		for r in range (len(self.__patches)):
			self.__patches[0,r].toggleRiver()
			self.__patches[1,r].toggleRiver()
			self.__grid[r,0] = 0
			self.__grid[r,1] = 0

	def generateCoords(self):
		r = random.randint(0,40)
		c = random.randint(2,40)
		return [r,c]

	def isPatchAvailable(self,coords):

		if self.__patches[coords[0], coords[1]].isRiver() == False and self.__patches[coords[0],coords[1]].isSettlement() == False:
			return True
		else:
			return False


	def setUpSettlements(self,settlement_list):
		#takes a list of settlements as a parameter
		counter = 0
		coords_list = []

		while(counter < len(settlement_list)):
			coords = self.generateCoords()
			if self.isPatchAvailable(coords) == True:
				settlement_list[counter].setCoordinates(coords) #set coords in settlement object [r,c]
				self.__patches[coords[0],coords[1]].toggleSettlement()
				coords_list.append(coords) #2d array - each element is a new set of coords of settlements
				#change block to a settlement in the plot (return list of coords to simulate)
				counter += 1
			else:
				coords = self.generateCoords()
		return coords_list

	def gridRecolour(self):
		for r in range(2,41):
			for c in range(0,41):
				num = int(10*round(self.__patches[r][c].inner.getFertility(), 1))
				if(num == 0):
					num += 1
				print(num, num == 0)###########testing to see whether there are any zeros
				self.__grid[c][r] = num
		#self.createRiver()

	def assignFertilityColour(fertility):
		#takes a string as a parameter
		#happens every tick
		pass

	def claimField(household):
		pass

	def harvest():
		#harvest
		pass

	def rentField():
		#rent
		pass

	def removeLink():
		#remove
		pass

	def enlargeSettlement(factor):
		#takes an int as a parameter
		pass

	def reduceSettlement(factor):
		##takes an int as a parameter
		pass

	def recolourHouseholds():
		#recolour
		pass

	def updatePlotValues(totHouseholds, totPopulation, ambition, competency):
		#update - REVISE THE METHOD THAT IS IN THE SIMULATE CLASS
		pass

	def clearAll(self):
		#clear everything and start new
		__lorenz_points = 0.0
		__gini_index_reserve = 0.0
		__avg_ambition = 0.0
		__avg_competency = 0.0
		__grid = np.empty((41,41), dtype= int)
		__patches = np.empty((41,41), dtype = object)
