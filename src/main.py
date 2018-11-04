from render import draw2d, on_keyPressed
from bentuk import objek
from OpenGL.GLUT import glutInit, glutInitDisplayMode, glutInitWindowSize, glutCreateWindow
from OpenGL.GLUT import glutInitWindowPosition, glutKeyboardFunc, glutDisplayFunc, glutIdleFunc, glutMainLoop
from OpenGL.GLUT import GLUT_RGBA, GLUT_DOUBLE, GLUT_ALPHA, GLUT_DEPTH
from config import config
from transformasi import *

import threading


def getInput():
    masukan = ['']
    while(masukan[0] != 'keluar'):
        masukan = input("> ").split(' ')
        if(masukan[0] == 'reset'):
            config.curMinX, config.curMaxX, config.curMinY, config.curMaxY, config.curMinZ, config.curMaxZ = - \
                10, 10, -10, 10, -10, 10
            config.objTest = objek(False)
        elif(masukan[0] == 'translasi'):
            if(config.is3D):
                pass
            else:
                if(len(masukan) == 3):
                    # Valid
                    dX, dY = int(masukan[1]), int(masukan[2])
                    config.objTest.animator.startAnimasi(translate(dX/30, dY/30))


if(__name__ == "__main__"):
    procInput = threading.Thread(target=getInput)
    procInput.start()
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(config.width, config.height)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("Tubes Algeo 2")
    glutKeyboardFunc(on_keyPressed)
    glutDisplayFunc(draw2d)
    glutIdleFunc(draw2d)
    glutMainLoop()
