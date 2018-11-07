from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from config import config
from transformasi import *

def refresh2d():
    glViewport(0, 0, config.width, config.height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(config.curMinX, config.curMaxX,
            config.curMinY, config.curMaxY, -10, 10)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(config.camX2D, config.camY2D, config.camZ2D,0, 0, 0, 1, 0)

def refresh3d():
    glViewport(0, 0, config.width, config.height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(config.curMinX, config.curMaxX,
            config.curMinY, config.curMaxY, -100, 100)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(config.camX3D, config.camY3D, config.camZ3D, 0, 0, 0, 0, 1, 0)


def garis(startX, startY, startZ, finishX, finishY, finishZ):
    glBegin(GL_LINES)
    glVertex3f(startX, startY, startZ)
    glVertex3f(finishX, finishY, finishZ)
    glEnd()


def gambarSumbu(is3D):
    if(is3D):
        glLineWidth(4)
        # Sumbu Negatif
        glColor3f(1, 1, 1)
        garis(config.curMinX, 0, 0, 0, 0, 0)
        garis(0, config.curMinY, 0, 0, 0, 0)
        garis(0, 0, config.curMinZ, 0, 0, 0)
        # Sumbu Positif
        glColor3f(1, 0, 0)
        garis(0, 0, 0, config.curMaxX, 0, 0)
        glColor3f(0, 1, 0)
        garis(0, 0, 0, 0, config.curMaxY, 0)
        glColor3f(0, 0, 1)
        garis(0, 0, 0, 0, 0, config.curMaxZ)
        glLineWidth(1)
    else:
        glLineWidth(4)
        glColor3f(1, 1, 1)
        garis(config.curMinX, 0, 0, config.curMaxX, 0, 0)
        garis(0, config.curMinY, 0, 0, config.curMaxY, 0)
        glLineWidth(1)


def gambarGrid(is3D):
    xy,xz,yz = config.xy,config.xz,config.yz
    if(is3D):
        dX = config.curMaxX-config.curMinX
        dY = config.curMaxY-config.curMinY
        dZ = config.curMaxZ-config.curMinZ
        gridX, gridY, gridZ = np.ceil(dX/10), np.ceil(dY/10), np.ceil(dZ/10)

        for i in range(6):
            glColor3f(xy[0],xy[1],xy[2])
            garis(config.curMinX, i*gridY, 0, config.curMaxX, i*gridY, 0)
            garis(config.curMinX, -i*gridY, 0, config.curMaxX, -i*gridY, 0)

            glColor3f(xz[0],xz[1],xz[2])
            garis(config.curMinX, 0, i*gridZ, config.curMaxX, 0, i*gridZ)
            garis(config.curMinX, 0, -i*gridZ, config.curMaxX, 0, -i*gridZ)
        for i in range(6):
            glColor3f(xy[0],xy[1],xy[2])
            garis(i*gridX, config.curMinY, 0, i*gridX, config.curMaxY, 0)
            garis(-i*gridX, config.curMinY, 0, -i*gridX, config.curMaxY, 0)

            glColor3f(yz[0],yz[1],yz[2])
            garis(0, config.curMinY, i*gridZ, 0, config.curMaxY, i*gridZ)
            garis(0, config.curMinY, -i*gridZ, 0, config.curMaxY, -i*gridZ)
        for i in range(6):
            glColor3f(xz[0],xz[1],xz[2])
            garis(i*gridX, 0, config.curMinZ, i*gridX, 0, config.curMaxZ)
            garis(-i*gridX, 0, config.curMinZ, -i*gridX, 0, config.curMaxZ)

            glColor3f(yz[0],yz[1],yz[2])
            garis(0, i*gridY, config.curMinZ, 0, i*gridY, config.curMaxZ)
            garis(0, -i*gridY, config.curMinZ, 0, -i*gridY, config.curMaxZ)
    else:
        glColor3f(xy[0],xy[1],xy[2])
        dX = config.curMaxX-config.curMinX
        dY = config.curMaxY-config.curMinY
        gridX, gridY = np.ceil(dX/10), np.ceil(dY/10)
        for i in range(10):
            garis(config.curMinX, i*gridY, 0, config.curMaxX, i*gridY, 0)
            garis(config.curMinX, -i*gridY, 0, config.curMaxX, -i*gridY, 0)
        for i in range(10):
            garis(i*gridX, config.curMinY, 0, i*gridX, config.curMaxY, 0)
            garis(-i*gridX, config.curMinY, 0, -i*gridX, config.curMaxY, 0)
    glColor3f(1,1,1)

def draw2d():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    if(config.is3D):
        refresh3d()
    else:
        refresh2d()

    config.objTest.gambar()
    gambarGrid(config.is3D)
    gambarSumbu(config.is3D)

    # Sampe sini
    glutSwapBuffers()
