import numpy as np
import tensorflow as tf

class histogramas:

	def __init__(self):
		self.nbins= tf.constant(255)
		self.rango_de_valores=tf.constant([0.0, 255.0])
		self.lista_histogramas= np.array([])
		self.lista_histogramas_normalizados=np.array([])

	"""
		Funcion encargada de devolver los histogramas
		resive una lista de frame
		almacena cada uno de los histogramas 
		en el parametro lista de histogramas
	"""

	def obtener_histogramas(self,lista_frame):
		lista_valores=np.array([])
		"""
		with tf.Session() as sess:

			for i in lista_frame:
				# convierte el tipo nparray a un valor en Tensorflow
				lista_valores=np.append(lista_valores,sess.run(tf.convert_to_tensor(i, dtype=tf.float32)))


		print(lista_valores[1])
		"""
		#calculo de histogramas
		with tf.Session() as sess:
			LH=[]
			for i in lista_frame:
				valor=sess.run(tf.convert_to_tensor(i, dtype=tf.float32))
				LH.append(sess.run(tf.histogram_fixed_width(valor,self.rango_de_valores,self.nbins)))

			self.lista_histogramas=np.array(LH)

			


	def normalizacion_histogramas(self,width,height):

		cantidad_pixeles=tf.constant(width*height,tf.float32)

		with tf.Session() as sess:
			LHN=[]
			for i in self.lista_histogramas:
				LH=sess.run(tf.convert_to_tensor(i))

				resultado= tf.div(cantidad_pixeles,LH)
				LHN.append(sess.run(resultado))	
			

			self.lista_histogramas_normalizados=np.array(LHN)

			

		

