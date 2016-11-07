import Application as ap
import numpy as np
import cv2 as cv
import Image as im
from matplotlib import pyplot as plt
from Slicer import Slicer

class Histogram:


	# A partir de la lista de frames, se toma un arreglo (numpy) de histogramas
	def CalculateArrayOfHistograms(self, framesList):
		histogramsList = []
		for frame in framesList:
			histogramsList.append(cv.calcHist([frame],[0],None,[255],[0.0,255.0]))
		return np.array(histogramsList)


	# Toma el rango de videos que se deben guardar, solo es usada por SaveHistogramList
	def TakeRange(self, truncateToParam, histListParam):
		if truncateToParam == -1:
			return len(histListParam)
		else:
			return truncateToParam


	# Cada uno de los histogramas se normaliza (Dividir cada histograma por el # de pixeles)
	def NormalizeArrayOfHistograms(self, arrayOfHistograms, amountOfPixels ):
		normalizedArrayOfHistograms = []
		for histogram in arrayOfHistograms:
			newNormalizedHistogram = np.multiply(1.0/amountOfPixels, histogram)
			normalizedArrayOfHistograms.append(newNormalizedHistogram)
		return normalizedArrayOfHistograms


	# Usada para obtener el parametro que necesita la funcion anterior
	def CalculateAmountOfPixels(self, sampleFrame):
		width, height = np.shape(sampleFrame)
		return width * height


	# Guarda todos los histogramas dentro de la carpeta por defecto presente en Application
	# truncateTo = para limitar la cantidad de histogramas que se quieren guardar (-1 -> Todos)
	def SaveHistogramList(self, histogramList, truncateTo = -1, histogramPath = ap.histogramsFolderPath):
		for histogramNumber in range(self.TakeRange(truncateTo, histogramList)):
			cv.imwrite(histogramPath + "Hist " + str(histogramNumber) + ".jpg", histogramList[histogramNumber])


	# Muestra un histograma en la ventana (Sirve para pruebas)
	def Plot(self, histogram):
		plt.hist(histogram);
		plt.show()
