from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from config import *
from transformasi import *


test = np.mat([[0,0,1],[100,0,1],[100,100,1]])

def interpolate(awal,akhir,persen):
    #interpolate berguna untuk mereturn hasil interpolasi nilai dari awal
    #hingga akhir saat sudah sejauh brp persen
    #interpolate(0,10,0.5) = 5
    return awal + (akhir-awal)*persen

def refresh2d(width, height):
    glViewport(0,0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, width, 0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def on_keyPressed(key,mouseX,mouseY):
    #TODO : Handle keypress di GUI
    global test    
    if(key == b'w'):
        test = transformPolygon(test,translate(0,50))
    elif(key == b'd'):
        test = transformPolygon(test,translate(50,0))
    elif(key == b'a'):
        test = transformPolygon(test,translate(-50,0))
    elif(key == b's'):
        test = transformPolygon(test,translate(0,-50))

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
    glLineWidth(2)
    #Gambar disini
    gambarPolygon(test,False)
    #Sampe sini
    glutSwapBuffers()