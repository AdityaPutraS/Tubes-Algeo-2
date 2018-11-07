import numpy as np
import bentuk
from random import randint
from transformasi import rotasi
# Setting program
class config:
    # Static Variable
    # Ukuran GUI
    width, height = 1000, 1000
    # nilai koordinat minimal X,Y,Z
    minX, maxX = -int(width/2), int(width/2)
    minY, maxY = minX, maxX
    minZ, maxZ = minX, maxX
    # 2D / 3D
    is3D = True
    # Nilai awal orthogonal
    curMinX, curMaxX, curMinY, curMaxY, curMinZ, curMaxZ = -10, 10, -10, 10, -10, 10
    # Nilai camera
    camX2D, camY2D,camZ2D = 0,0,5
    camX3D, camY3D, camZ3D = 5,5,5
    # Vector Camera
    vecCam3D = np.mat([camX3D,camY3D,camZ3D,1])
    # Nilai warna grid
    xy, xz,yz = [[randint(0,255)/255 for color in range(3)] for i in range(3)]
    # Navigasi
    navX, navY, navZ, navZoom = 1, 1, 1, 1
    #Default Object
    objTest = bentuk.objek(is3D)

    def putarCamX(derajat):
        #Memutar vector kamera 3D dengan sb X positif sebagai pusat
        pass
    def putarCamY(derajat):
        #Memutar vector kamera 3D dengan sb Y positif sebagai pusat
        pass
    def putarCamZ(derajat):
        #Memutar vector kamera 3D dengan sb Z positif sebagai pusat
        pass
