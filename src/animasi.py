from transformasi import transformPolygon
from config import maxKey
from queue import Queue

class animasi:

    def __init__(self,isAnimasi=False,keyframe=0,maxKeyframe=maxKey,matrixAnimasi=0):
        self.isAnimasi = isAnimasi
        self.keyframe = keyframe
        self.maxKeyframe = maxKeyframe
        self.matrixAnimasi = matrixAnimasi
        self.queueAnimasi = 
    def setMatrix(self,matrixAnimasi):
        self.matrixAnimasi = matrixAnimasi

    def animate(self,polygon):
        if(self.isAnimasi):
            if(self.keyframe >= self.maxKeyframe):
                self.isAnimasi = False
                self.keyframe = 0
                return polygon
            else:
                self.keyframe += 1
                return transformPolygon(polygon,self.matrixAnimasi)
        else:
            return polygon

    def startAnimasi(self,matrixAnimasi):
        #Cara pakai, test = animasi.startAnimasi(translate(10,2),test) <-Contoh
        self.isAnimasi = True
        self.setMatrix(matrixAnimasi)
    def pushAnimasi(self,matrixAnimasi):
        pass

    