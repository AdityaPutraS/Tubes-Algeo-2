import numpy as np
import bentuk
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
    is3D = False
    # Nilai awal orthogonal
    curMinX, curMaxX, curMinY, curMaxY, curMinZ, curMaxZ = -10, 10, -10, 10, -10, 10
    # Navigasi
    navX, navY, navZ, navZoom = 1, 1, 1, 1
    #Default Object
    objTest = bentuk.objek(is3D)
