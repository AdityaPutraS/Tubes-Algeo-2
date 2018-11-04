import numpy as np
import math

def translate(dx,dy,dz=0,is3D=False):
    if(is3D):
        return np.matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[dx,dy,dz,1]])
    else:
        return np.matrix([[1,0,0],[0,1,0],[dx,dy,1]])

def rotasi(degree,a=0,b=0, c=0, is3D=False) : #degree berlawan arah jarum jam terhadap titik(a,b)
	#masih belum
	#return np.matrix([math.cos(degree),math.sin(degree),0],[-1*math.sin(degree),math.cos(degree),0],[-1*a*math.cos(degree)+b*math.sin(degree)+m,-1*a*math.sin(degree)-b*math.cos(degree)+n,1])
    pass
def dilate(k, is3D=False):
	if(is3D):
		return np.matrix([[k,0,0,0],[0,k,0,0],[0,0,k,0],[0,0,0,1]])
	else:
		return np.matrix([[k,0,0],[0,k,0],[0,0,1]])

def reflect(a,b=0):
    #3Dmasih belum
    if (a=='x'):
        return np.matrix([[1,0,0],[0,-1,0],[0,0,1]])
    elif (a=='y'):
        return np.matrix([[-1,0,0],[0,1,0],[0,0,1]])
    elif (a=='y=x'):
        return np.matrix([[0,1,0], [1,0,0],[0,0,1]])
    elif (a=='y=-x'):
        return np.matrix([[0,-1,0], [-1,0,0],[0,0,1]])
    else: #point (a,b)
        return np.matrix([[-1,0,0], [0,-1,0],[2*a, 2*b,1]])

def shear(param,k):
    #3D skip dlu
    if(param=='x'):
        return([[1,0,0],[k,1,0],[0,0,1]])
    else: #y
        return([[1,k,0],[0,1,0],[0,0,1]])

def stretch(param,k):
    #3D skip dlu
    if(param=='x'):
        return([[1,0,0],[0,k,0],[0,0,1]])
    else: #y
        return([[k,0,0],[0,1,0],[0,0,1]])

def custom(a,b,c,d):
    #3D skip dlu
    return np.matrix([[a,c,0],[b,d,0],[0,0,1]])

def transformVertex(titik,matriks):
    return np.mat(titik) * np.mat(matriks)

def transformPolygon(listOfVertex,matriks):
    newList = []
    for v in listOfVertex:
        newList.append(transformVertex(v,matriks))
    return newList
