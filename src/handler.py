from config import config
from transformasi import *

def on_keyPressed(key, mouseX, mouseY):

    if(key == b'd'):
        config.curMaxX += config.navX
        config.curMinX += config.navX
        if(config.curMaxX > config.maxX):
            config.curMinX -= (config.curMaxX-config.maxX)
            config.curMaxX = config.maxX
    elif(key == b'a'):
        config.curMaxX -= config.navX
        config.curMinX -= config.navX
        if(config.curMinX < config.minX):
            config.curMaxX -= (config.minX-config.curMinX)
            config.curMinX = config.minX
    elif(key == b'w'):
        config.curMaxY += config.navY
        config.curMinY += config.navY
        if(config.curMaxY > config.maxY):
            config.curMinX -= (config.curMaxY-config.maxY)
            config.curMaxY = config.maxY
    elif(key == b's'):
        config.curMaxY -= config.navY
        config.curMinY -= config.navY
        if(config.curMinY < config.minY):
            config.curMaxY -= (config.minY-config.curMinY)
            config.curMinY = config.minY
    elif(key == b'q'):
        # Zoom in
        config.curMinX += config.navZoom
        config.curMaxX -= config.navZoom
        config.curMinY += config.navZoom
        config.curMaxY -= config.navZoom
    elif(key == b'e'):
        # Zoom out
        config.curMinX -= config.navZoom
        config.curMaxX += config.navZoom
        config.curMinY -= config.navZoom
        config.curMaxY += config.navZoom
    elif(key == b'8'):
        # Translasi ke atas
        config.objTest.animator.startAnimasi(translate(0, 5/30))
    elif(key == b'2'):
        # Translasi ke atas
        config.objTest.animator.startAnimasi(translate(0, -5/30))
    elif(key == b'4'):
        # Translasi ke atas
        config.objTest.animator.startAnimasi(translate(-5/30, 0))
    elif(key == b'6'):
        # Translasi ke atas
        config.objTest.animator.startAnimasi(translate(5/30, 0))