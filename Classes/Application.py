from Histogram import Histogram
from Slicer import Slicer
from Bhattacharyya import Bhattacharyya

# Rutas que el programa usará por defecto
videoPath = "/home/julian/Github/Cuts_Detector_Python/Source/Video.mp4"
framesFolderPath = "/home/julian/Github/Cuts_Detector_Python/Frames/"
histogramsFolderPath = "/home/julian/Github/Cuts_Detector_Python/Histograms/"

h = Histogram()
s = Slicer()
b = Bhattacharyya()


# Ejecucion del programa
normalizedFramesList = s.SliceVideo(videoUntil = 50)
arrayOfHistograms = h.CalculateArrayOfHistograms(normalizedFramesList)
amountOfPixels = h.CalculateAmountOfPixels(normalizedFramesList[0])
normalizedHistograms = h.NormalizeArrayOfHistograms(arrayOfHistograms, amountOfPixels)
arrayOfDissimilitudes = b.CalculateAllDissimilitudes(normalizedHistograms)


# Pruebas
print arrayOfDissimilitudes
import random
h.Plot(normalizedHistograms[random.choice(range(50))])