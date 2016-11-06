from histogramas import histogramas
from video import video
import numpy as np

class controlador:

	def __init__(self):
		self.HG=histogramas()
		self.Video=video()

	def inicio(self):
		
		self.Video.leer_video("Dissolve1-15.mp4")
		
		self.HG.obtener_histogramas(self.Video.frame_List)
		
		self.HG.normalizacion_histogramas(self.Video.width,self.Video.height)


		print(np.sum(np.array(self.HG.lista_histogramas_normalizados[0])))

	