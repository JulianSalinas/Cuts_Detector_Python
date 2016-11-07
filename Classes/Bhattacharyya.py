from math import sqrt
from math import pow
import numpy as np

class Bhattacharyya:


	# Crear un arreglo con todas las disimilitudes entre los histogramas
	def CalculateAllDissimilitudes(self, arrayOfHistograms):
		listOfDissimilitudes = []
		for hIndex in range(len(arrayOfHistograms) - 1 ):
			h1 = arrayOfHistograms[hIndex]
			h2 = arrayOfHistograms[hIndex+1]
			newDissimilitude = self.CalculateDissimilitude(h1, h2)
			listOfDissimilitudes.append(newDissimilitude)
		return np.array(listOfDissimilitudes)


	# Disimilitud entre dos histogramas
	def CalculateDissimilitude(self, h1, h2):
		alpha = self.CalculateAlpha(h1,h2)
		beta = self.CalcularBeta(h1,h2)
		return sqrt(1-(alpha*beta))


	# Calcula el coeficiente de normalizacion
	def CalculateAlpha(self, h1, h2):
		return 1.0 / (sqrt(np.mean(h1)*np.mean(h2)*pow(255.0,2.0)))


	# Calcula el coeficiente de Bhattacharyya
	def CalcularBeta(self, h1, h2):
		beta = 0
		for z in range(255): beta += sqrt(h1[z] * h2[z])
		return beta


