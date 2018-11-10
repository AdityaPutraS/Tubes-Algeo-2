import numpy as np
from animasi import animasi
import OpenGL.GL as gl
from random import randint

def lingkaran(x, y, r):
    hasil = []
    for i in range(0, 360):
        hasil.append(
            np.mat([[x+r*np.cos(i/180 * np.pi), y-r*np.sin(i/180 * np.pi), 1]]))
    return hasil


def gambarPolygon(listOfVertex, is3D,warnaKubus=[],listOfTriangle=[]):
    gl.glColor3f(warnaKubus[0][0],warnaKubus[0][1],warnaKubus[0][2])
    if(is3D):
        # Handle untuk 3D
        index = 0
        for triangle in listOfTriangle:
            r,g,b = warnaKubus[index][0],warnaKubus[index][1],warnaKubus[index][2]
            gl.glColor3f(r,g,b)
            gl.glBegin(gl.GL_POLYGON)
            for v in triangle:
                gl.glVertex3f(listOfVertex[v].item(0),listOfVertex[v].item(1),listOfVertex[v].item(2))
            gl.glEnd()
            index += 1
    else:
        # Handle untuk 2D
        gl.glBegin(gl.GL_POLYGON)
        for v in listOfVertex:
            gl.glVertex2f(v.item(0), v.item(1))
        gl.glEnd()


class objek:
    # Default Value
    listVertex2D = [np.mat([-1, -1,0, 1]), np.mat([1, -1,0, 1]),
                    np.mat([1, 1,0, 1]), np.mat([-1, 1,0, 1])]
    listVertex3D = [np.mat([-1, -1, 1, 1]), np.mat([1, -1, 1, 1]), np.mat([1, -1, -1, 1]), np.mat([-1, -1, -1, 1]),
                    np.mat([-1, 1, -1, 1]), np.mat([-1, 1, 1, 1]), np.mat([1, 1, 1, 1]), np.mat([1, 1, -1, 1])]
    listSegitiga3D = [(0,1,2),(0,2,3),(0,1,6),(0,5,6),(1,2,7),(1,6,7),(2,7,4),(2,3,4),(0,3,4),(0,5,4),(4,5,6),(4,6,7)]

    def __init__(self, is3D=False, listVertex=[]):
        self.is3D = is3D   
        if(is3D):
            self.listVertex = objek.listVertex3D
        else:
            self.listVertex = objek.listVertex2D
        self.animator = animasi()
        #Generate Warna
        self.warnaKubus = []
        for i in range(len(self.listSegitiga3D)):
            r,g,b = randint(0,255)/255,randint(0,255)/255,randint(0,255)/255
            temp = [r,g,b]
            self.warnaKubus.append(temp)
            self.warnaKubus.append(temp)
    def gambar(self):
        self.listVertex = self.animator.animate(self.listVertex)
        gambarPolygon(self.listVertex, self.is3D,self.warnaKubus,self.listSegitiga3D)
