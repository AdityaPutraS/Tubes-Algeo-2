import numpy as np
from animasi import animasi
import OpenGL.GL as gl

def lingkaran(x, y, r):
    hasil = []
    for i in range(0, 360):
        hasil.append(
            np.mat([[x+r*np.cos(i/180 * np.pi), y-r*np.sin(i/180 * np.pi), 1]]))
    return hasil


def gambarPolygon(listOfVertex, is3D, r, g, b):
    gl.glColor3f(r, g, b)
    gl.glBegin(gl.GL_POLYGON)
    if(is3D):
        # Handle untuk 3D
        for v in listOfVertex:
            gl.glVertex3f(v.item(0), v.item(1), v.item(2))
    else:
        # Handle untuk 2D
        for v in listOfVertex:
            gl.glVertex2f(v.item(0), v.item(1))
    gl.glEnd()


class objek:
    # Default Value
    listVertex2D = [np.mat([-1, -1, 1]), np.mat([1, -1, 1]),
                    np.mat([1, 1, 1]), np.mat([-1, 1, 1])]
    listVertex3D = [np.mat([-1, -1, 1, 1]), np.mat([1, -1, 1, 1]), np.mat([1, -1, -1, 1]), np.mat([-1, -1, -1, 1]),
                    np.mat([-1, 1, -1, 1]), np.mat([-1, 1, 1, 1]), np.mat([1, 1, 1, 1]), np.mat([1, 1, -1, 1])]

    def __init__(self, is3D=False, listVertex=[], r=0, g=255, b=0):
        self.is3D = is3D
        if(is3D):
            self.listVertex = objek.listVertex3D
        else:
            self.listVertex = objek.listVertex2D
        self.animator = animasi()
        self.r, self.g, self.b = r, g, b

    def gambar(self):
        self.listVertex = self.animator.animate(self.listVertex)
        gambarPolygon(self.listVertex, self.is3D, self.r, self.g, self.b)
