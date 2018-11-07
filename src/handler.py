from config import config
from transformasi import *

def on_keyPressed(key, mouseX, mouseY):

    if(key == b'd'):
        if(config.is3D):
            config.camX3D += config.navX
            config.putarCamY(30)
        else:
            config.curMaxX += config.navX
            config.curMinX += config.navX
            if(config.curMaxX > config.maxX):
                config.curMinX -= (config.curMaxX-config.maxX)
                config.curMaxX = config.maxX
    elif(key == b'a'):
        if(config.is3D):
            config.camX3D -= config.navX
        else:
            config.curMaxX -= config.navX
            config.curMinX -= config.navX
            if(config.curMinX < config.minX):
                config.curMaxX -= (config.minX-config.curMinX)
                config.curMinX = config.minX
    elif(key == b'w'):
        if(config.is3D):
            config.camY3D += config.navY
        else:
            config.curMaxY += config.navY
            config.curMinY += config.navY
            if(config.curMaxY > config.maxY):
                config.curMinX -= (config.curMaxY-config.maxY)
                config.curMaxY = config.maxY
    elif(key == b's'):
        if(config.is3D):
            config.camY3D -= config.navY
        else:
            config.curMaxY -= config.navY
            config.curMinY -= config.navY
            if(config.curMinY < config.minY):
                config.curMaxY -= (config.minY-config.curMinY)
                config.curMinY = config.minY
    elif(key == b'q'):
        if(config.is3D):
            pass
        else:
            # Zoom in
            config.curMinX += config.navZoom
            config.curMaxX -= config.navZoom
            config.curMinY += config.navZoom
            config.curMaxY -= config.navZoom
    elif(key == b'e'):
        if(config.is3D):
            pass
        else:
            # Zoom out
            config.curMinX -= config.navZoom
            config.curMaxX += config.navZoom
            config.curMinY -= config.navZoom
            config.curMaxY += config.navZoom
    elif(key == b'8'):
        # Translasi ke atas
        config.objTest.animator.startAnimasi(translate(0, 5/30,0,config.is3D))
    elif(key == b'2'):
        # Translasi ke atas
        config.objTest.animator.startAnimasi(translate(0, -5/30,0,config.is3D))
    elif(key == b'4'):
        # Translasi ke atas
        config.objTest.animator.startAnimasi(translate(-5/30, 0,0,config.is3D))
    elif(key == b'6'):
        # Translasi ke atas
        config.objTest.animator.startAnimasi(translate(5/30, 0,0,config.is3D))