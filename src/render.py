from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from config import *
from transformasi import *


test = np.mat([[0,0,1],[100,0,1],[100,100,1],[0,100,1]])
keyframe = 0
polygonTemp = test
matrixAnimasi = 0
animasi = False

def interpolate(awal,akhir,persen):
    #interpolate berguna untuk mereturn hasil interpolasi nilai dari awal
    #hingga akhir saat sudah sejauh brp persen
    #interpolate(0,10,0.5) = 5
    return awal + (akhir-awal)*persen

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def on_keyPressed(key,mouseX,mouseY):
    #TODO : Handle keypress di GUI
    global matrixAnimasi,animasi,keyframe,polygonTemp
    if(key == b'w'):
        animasi = True
        keyframe = 0
        matrixAnimasi = translate(0,100/30)
    elif(key == b'd'):
        animasi = True
        keyframe = 0
        matrixAnimasi = translate(100/30,0)
    elif(key == b'a'):
        animasi = True
        keyframe = 0
        matrixAnimasi = translate(-100/30,0)
    elif(key == b's'):
        animasi = True
        keyframe = 0
        matrixAnimasi = translate(0,-100/30)

def gambarPolygon(listOfVertex, is3D):
    glBegin(GL_POLYGON)
    if(is3D):
        #Handle untuk 3D
        for v in listOfVertex:
            glVertex3f(v.item(0),v.item(1),v.item(2))
    else:
        #Handle untuk 2D
        for v in listOfVertex:
            glVertex2f(v.item(0),v.item(1))
    glEnd()
    
def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    refresh2d(width,height)
    glColor3f(0.0, 0.0, 1.0)
    #Gambar disini
    global test,animasi,keyframe,polygonTemp
    if(animasi):
        if(keyframe == 31):
            animasi = False
            keyframe = 0
        else:
            test = transformPolygon(test,matrixAnimasi)
            keyframe += 1
    gambarPolygon(test,False)
    print(test)
    #Sampe sini
    glutSwapBuffers()