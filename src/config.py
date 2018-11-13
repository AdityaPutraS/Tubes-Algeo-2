maxKey = 30
import numpy as np
import bentuk
from random import randint
from transformasi import rotasi,rotasiY,dilate
# Setting program
class config:
    # Static Variable
    # Ukuran GUI
    width, height = 1000, 1000
    #Program jalan
    jalan = True
    # nilai koordinat minimal X,Y,Z
    minX, maxX = -int(width/2), int(width/2)
    minY, maxY = minX, maxX
    minZ, maxZ = minX, maxX
    # 2D / 3D
    is3D = True
    # Nilai awal orthogonal
    curMinX, curMaxX, curMinY, curMaxY, curMinZ, curMaxZ = -10, 10, -10, 10, -10, 10
    # Nilai camera
    camX2D, camY2D,camZ2D = 0.0,0.0,5.0
    camX3D, camY3D, camZ3D = 5.0,5.0,5.0
    # Vector Camera
    vecCam3D = np.mat([[camX3D,camY3D,camZ3D,1]])
    #TegakLurus = Proyeksi Vector Cam lalu diputar 90 derajat counterclockwise
    tegakLurusCam3D = np.mat([[camX3D,0,camZ3D,1]]) * rotasiY(90)
    # Nilai warna grid
    xy, xz,yz = [[randint(0,255)/255 for color in range(3)] for i in range(3)]
    # Navigasi
    navX, navY, navZ, navZoom = 1, 1, 1, 1.1
    navPutar = 5
    #Animasi
    maxKeyFrame = maxKey
    #Default Object
    objTest = bentuk.objek(is3D)
    listOfVertex = []
    default = True
    def initAwal(is3D,listOfVertex=[],default=True):
        config.is3D = is3D
        config.listOfVertex = listOfVertex
        config.default = default
        config.objTest = bentuk.objek(is3D,listOfVertex,default)

    def reset():
        config.vecCam3D = np.mat([[config.camX3D,config.camY3D,config.camZ3D,1]])
        config.tegakLurusCam3D = np.mat([[config.camX3D,0,config.camZ3D,1]]) * rotasiY(90)
        config.objTest = bentuk.objek(config.is3D,config.listOfVertex,config.default)

    def putarCamY(derajat):
        #Memutar vector kamera 3D dengan sb Y positif sebagai pusat
        config.vecCam3D *= rotasiY(derajat)
        config.tegakLurusCam3D *= rotasiY(derajat)
    def putarCam(derajat,vx,vy,vz):
        config.vecCam3D *= rotasi(derajat,vx,vy,vz)
    def zoomCam(k):
        config.vecCam3D *= dilate(k,config.is3D)
