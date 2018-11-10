from config import config
from transformasi import *

def on_keyPressed(key, mouseX, mouseY):

    if(key == b'd'):
        if(config.is3D):
            config.putarCamY(-config.navPutar)
        else:
            config.curMaxX += config.navX
            config.curMinX += config.navX
            if(config.curMaxX > config.maxX):
                config.curMinX -= (config.curMaxX-config.maxX)
                config.curMaxX = config.maxX
    elif(key == b'a'):
        if(config.is3D):
            config.putarCamY(config.navPutar)
        else:
            config.curMaxX -= config.navX
            config.curMinX -= config.navX
            if(config.curMinX < config.minX):
                config.curMaxX -= (config.minX-config.curMinX)
                config.curMinX = config.minX
    elif(key == b'w'):
        if(config.is3D):
            config.putarCam(config.navPutar,config.tegakLurusCam3D.item(0),config.tegakLurusCam3D.item(1),config.tegakLurusCam3D.item(2))
        else:
            config.curMaxY += config.navY
            config.curMinY += config.navY
            if(config.curMaxY > config.maxY):
                config.curMinX -= (config.curMaxY-config.maxY)
                config.curMaxY = config.maxY
    elif(key == b's'):
        if(config.is3D):
            config.putarCam(-config.navPutar,config.tegakLurusCam3D.item(0),config.tegakLurusCam3D.item(1),config.tegakLurusCam3D.item(2))
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
        config.objTest.animator.startAnimasi(translate(0, 5/config.maxKeyFrame,0))
    elif(key == b'2'):
        # Translasi ke atas
        config.objTest.animator.startAnimasi(translate(0, -5/config.maxKeyFrame,0))
    elif(key == b'4'):
        # Translasi ke atas
        config.objTest.animator.startAnimasi(translate(-5/config.maxKeyFrame, 0,0))
    elif(key == b'6'):
        # Translasi ke atas
        config.objTest.animator.startAnimasi(translate(5/config.maxKeyFrame, 0,0))