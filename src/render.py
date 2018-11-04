from OpenGL.GL import *
from OpenGL.GLUT import glutSwapBuffers
import numpy as np
from config import config
from transformasi import *


def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    glOrtho(config.curMinX, config.curMaxX,
            config.curMinY, config.curMaxY, 0, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def garis(startX, startY, startZ, finishX, finishY, finishZ):
    glBegin(GL_LINES)
    glVertex3f(startX, startY, startZ)
    glVertex3f(finishX, finishY, finishZ)
    glEnd()


def gambarSumbu(is3D):
    if(is3D):
        pass
    else:
        glLineWidth(4)
        glColor3f(255, 255, 255)
        garis(config.curMinX, 0, 0, config.curMaxX, 0, 0)
        garis(0, config.curMinY, 0, 0, config.curMaxY, 0)
        glLineWidth(1)
def gambarGrid(is3D):
    if(is3D):
        pass
    else:
        #Ukuran grid = deltaX // 10
        dX = config.curMaxX-config.curMinX
        dY = config.curMaxY-config.curMinY
        gridX,gridY = np.ceil(dX/10), np.ceil(dY/10)
        for i in range(10):
            garis(config.curMinX,i*gridY,0,config.curMaxX,i*gridY,0)
            garis(config.curMinX,-i*gridY,0,config.curMaxX,-i*gridY,0)
        for i in range(10):
            garis(i*gridX,config.curMinY,0,i*gridX,config.curMaxY,0)
            garis(-i*gridX,config.curMinY,0,-i*gridX,config.curMaxY,0)

def draw2d():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    refresh2d(config.width, config.height)
    gambarSumbu(False)
    gambarGrid(False)
    config.objTest.gambar()
    # Sampe sini
    glutSwapBuffers()
