import Application as ap
import numpy as np
import cv2 as cv

class Slicer:


    # Abre el video desde la ruta por defecto presente en Application
    def ReadFromSource(self, videoPath = ap.videoPath):
        return cv.VideoCapture(videoPath)


    # Lee cada frame del videoCapture
    # truncateTo = especifica cuantos frames se quieren extraer ( -1 -> Todos )
    def ListFramesRGB(self, videoCapture, truncateTo = -1):
        success = True
        framesList = []
        count = 0
        while success:
            success, frame = videoCapture.read()
            if success : framesList.append(frame)
            if count == truncateTo - 1 : success = False
            count += 1
        return framesList


    # Convierte la lista de frames de RGB a H (de HSV)
    def ListFramesH(self, framesList):
        framesListH = []
        for frame in framesList:
            framesListH.append(self.GetHLayerFromRGB(frame))
        return framesListH


    # Convierte y toma la capa H  de HSV a partir de un frame en RGB
    def GetHLayerFromRGB(self, frameRGB):
        HSV = cv.cvtColor(frameRGB, cv.COLOR_RGB2HSV)
        return np.array(HSV[:, :, 0])


    # Guarda todos los frames dentro de la carpeta por defecto presente en Application
    # truncateTo = para limitar la cantidad de frames que se quieren guardar (-1 -> Todos)
    def SaveFrameList(self, framesList, truncateTo = -1, framePath = ap.framesFolderPath):
        for frameNumber in range(self.TakeRange(truncateTo,framesList)):
            cv.imwrite(framePath + "Frame " + str(frameNumber) + ".jpg", framesList[frameNumber])


    # Toma el rango de videos que se deben guardar, solo es usada por SaveFrameList
    def TakeRange(self, truncateToParam, framesListParam):
        if truncateToParam == -1 : return len(framesListParam)
        else: return truncateToParam


    # Toma una lista con la capa H de los frames y las coloca entre 0 y 255
    def NormalizeLayersH(self, framesListH):
        normalizedFramesH = []
        for frame in framesListH:
            normImg = cv.normalize(frame, 0, 255, norm_type = cv.NORM_MINMAX)
            normalizedFramesH.append(normImg)
        return normalizedFramesH

    # Usada para obtener el parametro que necesita la funcion anterior
    def CalculateAmountOfPixels(self, sampleFrame):
        width, height = np.shape(sampleFrame)
        return width * height


    # Parte un video de entrada en varios frames H
    # videoUntil = especifica cuantos frames procesar ( -1 -> Todos)
    # saveUntil = especifica cuantos frames guardar, saveUntil <= videoUntil
    def SliceVideo (self, videoPath = ap.videoPath, videoUntil = -1, saveUntil = -1):
        print "Reading video from " + videoPath + "..."
        videoCapture = self.ReadFromSource(videoPath)
        print "Listing RGB frames..."
        framesList = self.ListFramesRGB(videoCapture, videoUntil)
        print "Extracting layers H..."
        framesListH = self.ListFramesH(framesList)
        print "Normalizing layers to (0,255)..."
        normalizedFramesListH = self.NormalizeLayersH(framesListH)
        print "Saving frames H into " + op.framesFolderPath + "..."
        if saveUntil > 0 : self.SaveFrameList(normalizedFramesListH, saveUntil)
        return normalizedFramesListH
