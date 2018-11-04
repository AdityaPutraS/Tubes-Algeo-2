from OpenGL.GL import *
from OpenGL.GLUT import glutSwapBuffers
import numpy as np
from config import *
from bentuk import objek
from transformasi import *

test = [[-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]]
test = [np.mat([x]) for x in test]
startGambar = False
r, g, b = 0, 1.0, 0

objTest = objek(test,False)

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    glOrtho(curMinX, curMaxX, curMinY, curMaxY, 0, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def on_keyPressed(key, mouseX, mouseY):
    print(key)
    global curMaxX,curMinX,curMaxY,curMinY
    global navX,navY,navZ,navZoom

    if(key == b'd'):
        curMaxX += navX
        curMinX += navX
        if(curMaxX > maxX):
            curMinX -= (curMaxX-maxX)
            curMaxX = maxX
    elif(key == b'a'):
        curMaxX -= navX
        curMinX -= navX
        if(curMinX < minX):
            curMaxX -= (minX-curMinX)
            curMinX = minX
    elif(key == b'w'):
        curMaxY += navY
        curMinY += navY
        if(curMaxY > maxY):
            curMinX -= (curMaxY-maxY)
            curMaxY = maxY
    elif(key == b's'):
        curMaxY -= navY
        curMinY -= navY
        if(curMinY < minY):
            curMaxY -= (minY-curMinY)
            curMinY = minY
    elif(key == b'q'):
        #Zoom in
        curMinX += navZoom
        curMaxX -= navZoom
        curMinY += navZoom
        curMaxY -= navZoom
    elif(key == b'e'):
        #Zoom out
        curMinX -= navZoom
        curMaxX += navZoom
        curMinY -= navZoom
        curMaxY += navZoom
    elif(key == b'8'):
        #Translasi ke atas
        objTest.animator.startAnimasi(translate(0,5/30))
    elif(key == b'2'):
        #Translasi ke atas
        objTest.animator.startAnimasi(translate(0,-5/30))
    elif(key == b'4'):
        #Translasi ke atas
        objTest.animator.startAnimasi(translate(-5/30,0))
    elif(key == b'6'):
        #Translasi ke atas
        objTest.animator.startAnimasi(translate(5/30,0))

def garis(startX,startY,startZ,finishX,finishY,finishZ):
    glBegin(GL_LINES)
    glVertex3f(startX,startY,startZ)
    glVertex3f(finishX,finishY,finishZ)
    glEnd()

def gambarSumbu(is3D):
    if(is3D):
        pass
    else:
        glColor3f(255,255,255)
        garis(curMinX,0,0,curMaxX,0,0)
        garis(0,curMinY,0,0,curMaxY,0)

def draw2d():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    refresh2d(width, height)
    gambarSumbu(False)
    objTest.gambar()

    # Sampe sini
    glutSwapBuffers()
