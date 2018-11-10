from render import draw
from bentuk import objek
import handler
from OpenGL.GLUT import glutInit, glutInitDisplayMode, glutInitWindowSize, glutCreateWindow
from OpenGL.GLUT import glutInitWindowPosition, glutKeyboardFunc, glutDisplayFunc, glutIdleFunc, glutMainLoop
from OpenGL.GLUT import GLUT_RGBA, GLUT_DOUBLE, GLUT_ALPHA, GLUT_DEPTH
from config import config
from transformasi import *
from ProcInput import ProcInput

import threading

if(__name__ == "__main__"):
    stis3D = input("Apakah anda ingin melakukan transformasi 3D?(Y = Yes, N = No) ")
    is3D = (stis3D == "Y") or (stis3D == "y")
    config.initAwal(is3D)
    #MultiThreading Boi
    procInput = threading.Thread(target=ProcInput,args=(config.is3D,))
    procInput.start()
    #GUI
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(config.width, config.height)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("Tubes Algeo 2")
    #Event Handler & Draw function
    glutKeyboardFunc(handler.on_keyPressed)
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutMainLoop()
