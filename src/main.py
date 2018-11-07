from render import draw2d
from bentuk import objek
import handler
from OpenGL.GLUT import glutInit, glutInitDisplayMode, glutInitWindowSize, glutCreateWindow
from OpenGL.GLUT import glutInitWindowPosition, glutKeyboardFunc, glutDisplayFunc, glutIdleFunc, glutMainLoop
from OpenGL.GLUT import GLUT_RGBA, GLUT_DOUBLE, GLUT_ALPHA, GLUT_DEPTH
from config import config
from transformasi import *

import threading


def getInput():
    masukan = ['']
    global config
    while(masukan[0] != 'keluar'):
        masukan = input("> ").split(' ')
        if(masukan[0] == 'reset'):
            config.curMinX, config.curMaxX, config.curMinY, config.curMaxY, config.curMinZ, config.curMaxZ = - \
                10, 10, -10, 10, -10, 10
            config.objTest = objek(config.is3D)
        elif(masukan[0] == '3d'):
            config.is3D = True
            config.objTest = objek(True)
        elif(masukan[0] == '2d'):
            config.is3D = False
            config.objTest = objek(False)
        elif(masukan[0] == 'translasi'):
            if(config.is3D):
                pass
            else:
                if(len(masukan) == 3):
                    # Valid
                    dX, dY = float(masukan[1]), float(masukan[2])
                    config.objTest.animator.startAnimasi(translate(dX/30, dY/30))
                else:
                    #Tidak Valid
                    print("Masukan tidak valid")
        elif(masukan[0] == 'dilatasi'):
            if(config.is3D):
                pass
            else:
                if(len(masukan) == 2):
                    # Valid
                    k = float(masukan[1])
                    config.objTest.animator.startAnimasi(dilate((k**(1/30))))
                else:
                    #Tidak Valid
                    print("Masukan tidak valid")



if(__name__ == "__main__"):
    #MultiThreading Boi
    procInput = threading.Thread(target=getInput)
    procInput.start()
    #GUI
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(config.width, config.height)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("Tubes Algeo 2")
    #Event Handler & Draw function
    glutKeyboardFunc(handler.on_keyPressed)
    glutDisplayFunc(draw2d)
    glutIdleFunc(draw2d)
    glutMainLoop()
