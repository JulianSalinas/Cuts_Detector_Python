import numpy as np
import cv2

class video:

	def __init__(self):
		self.frame_List=[]
		self.video = None
		self.width = 0
		self.height =0


	def leer_video(self,nombre_video):
		self.video=cv2.VideoCapture(nombre_video)

		valor=True
		i=0
		while valor:
			ret,frame = self.video.read()
			if ret:
				HSV=cv2.cvtColor(frame,cv2.COLOR_RGB2HSV)
				self.frame_List.append(np.array(HSV[:,:,0]))
				i=i+1
				if 4==i:
					valor=False
			else:
				valor=ret

		self.width,self.height=np.shape(self.frame_List[0])