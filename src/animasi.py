from transformasi import transformPolygon
from config import maxKey
from queue import Queue

class animasi:

    def __init__(self,isAnimasi=False,keyframe=0,maxKeyframe=maxKey,matrixAnimasi=0):
        self.isAnimasi = isAnimasi
        self.keyframe = keyframe
        self.maxKeyframe = maxKeyframe
        self.matrixAnimasi = matrixAnimasi
        self.queueAnimasi = Queue()
        
    def setMatrix(self,matrixAnimasi):
        self.matrixAnimasi = matrixAnimasi

    def animate(self,polygon):
        if(self.isAnimasi):
            if(self.keyframe >= self.maxKeyframe):
                if(not(self.isAnimasiEmpty())):
                    #Ada animasi lagi yang harus di animasikan
                    tupleQueue = self.popAnimasi()
                    self.startAnimasi(tupleQueue[0],tupleQueue[1])
                else:
                    #Tidak ada
                    self.keyframe = 0
                    self.isAnimasi = False
                return polygon
            else:
                self.keyframe += 1
                return transformPolygon(polygon,self.matrixAnimasi)
        else:
            if(not(self.isAnimasiEmpty())):
                #Ada animasi lagi yang harus di animasikan
                tupleQueue = self.popAnimasi()
                self.startAnimasi(tupleQueue[0],tupleQueue[1])
            return polygon

    def startAnimasi(self,matrixAnimasi,langsung=False):
        #Cara pakai, test = animasi.startAnimasi(translate(10,2),test) <-Contoh
        self.isAnimasi = True
        self.setMatrix(matrixAnimasi)
        if(langsung):
            self.keyframe = self.maxKeyframe-1
        else:
            self.keyframe = 0
    def pushAnimasi(self,matrixAnimasi):
        self.queueAnimasi.put(matrixAnimasi)
    def popAnimasi(self):
        return self.queueAnimasi.get()
    def isAnimasiEmpty(self):
        return self.queueAnimasi.empty()
    