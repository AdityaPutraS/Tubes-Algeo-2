import numpy as np

def translate(dx,dy,dz=0,is3D=False):
    if(is3D):
        return np.matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[dx,dy,dz,1]])
    else:
        return np.matrix([[1,0,0],[0,1,0],[dx,dy,1]])

def transformVertex(titik,matriks):
    return np.mat(titik) * np.mat(matriks)

def transformPolygon(listOfVertex,matriks):
    newList = []
    for v in listOfVertex:
        newList.append(transformVertex(v,matriks))
    return newList