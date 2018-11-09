import numpy as np
import math

def translate(dx,dy,dz=0,is3D=False):
    if(is3D):
        return np.matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[dx,dy,dz,1]])
    else:
        return np.matrix([[1,0,0],[0,1,0],[dx,dy,1]])

def rotasi(deg,a=0,b=0, c=0) : #degree berlawan arah jarum jam terhadap titik(a,b)
	return np.matrix([math.cos(deg),math.sin(deg),0],[-1*math.sin(deg),math.cos(deg),0],[-1*a*math.cos(deg)+b*math.sin(deg)+m,-1*a*math.sin(deg)-b*math.cos(deg)+n,1])

#asumsi ak make axis Z positif arah keluar layar, negatif masuk ke layar
#rotasi 3D dibawah ini selalu counter-clockwise
def rotasiX(deg) :
    # 1 0 0 0
    # 0 cos sin 0
    # 0 -sin cos 0
    # 0 0 0 1
    return np.matrix([1,0,0,0],[0, math.cos(deg), math.sin(deg),0],[0,-1*math.sin(deg), math.cos(deg), 0],[0,0,0,1])

def rotasiY(deg) :
    # cos 0 sin 0
    # 0 1 0 0
    # -sin 0 cos 0
    # 0 0 0 1
    return np.matrix([math.cos(deg),0,math.sin(deg),0],[0, 1, 0,0],[0,-1*math.sin(deg), 0, math.cos(deg), 0],[0,0,0,1])

def rotasiZ(deg) :
    # cos sin 0 0
    # -sin cos 0 0
    # 0 0 1 0
    # 0 0 0 1
    return np.matrix([math.cos(deg), math.sin(deg),0,0],[-1*math.sin(deg), math.cos(deg), 0,0],[0,0,1,0],[0,0,0,1])

def dilate(k, is3D=False):
	if(is3D):
		return np.matrix([k,0,0,0],[0,k,0,0],[0,0,k,0],[0,0,0,1])
	else:
		return np.matrix([k,0,0],[0,k,0],[0,0,1])

def reflect(a,b=0):#a bisa sebagai string atau titik
        if (a=='x'):
            return np.matrix([1,0,0],[0,-1,0],[0,0,1])
        elif (a=='y'):
            return np.matrix([-1,0,0],[0,1,0],[0,0,1])
        elif (a=='y=x'):
            return np.matrix([0,1,0], [1,0,0],[0,0,1])
        elif (a=='y=-x'):
            return np.matrix([0,-1,0], [-1,0,0],[0,0,1])
        else: #point (a,b)
            return np.matrix([-1,0,0], [0,-1,0],[2*a, 2*b,1])

def reflect3D(s):
        if (s=='xz'):
            return np.matrix([1,0,0,0],[0,-1,0,0],[0,0,1,0],[0,0,0,1])
        elif (s=='yz'):
            return np.matrix([-1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1])
        elif (s=='xy'):
            return np.matrix([1,0,0,0],[0,1,0,0],[0,0,-1,0],[0,0,0,1])

def shear(param,k):
    if(param=='x'):
        return([1,k,0],[0,1,0],[0,0,1])
    else: #y
        return([1,0,0],[k,1,0],[0,0,1])

def shear3D(param,k):
    if(param=='x'):
        return([1,k,k,0],[0,1,0,0],[0,0,1,0][0,0,0,1])
    elif (param=='y'): #y
        return([1,0,0,0],[k,1,k,0],[0,0,1,0],[0,0,0,1])
    else :
        return([1,0,0,0],[0,1,0,0],[k,k,1,0],[0,0,0,1])


def stretch(param,k):
    if(param=='x'):
        return([1,0,0],[0,k,0],[0,0,1])
    else: #y
        return([k,0,0],[0,1,0],[0,0,1])

def stretch3D(param,k):
    if(param=='x'):#horizontal
        return([1,0,0,0],[0,k,0,0],[0,0,k,0],[0,0,0,1])
    elif (param=='y'): #vertical
        return([k,0,0,0],[0,1,0,0],[0,0,k,0],[0,0,0,1])
    elif (param=='z'):
        return([k,0,0,0],[0,k,0,0],[0,0,1,0],[0,0,0,1])

def custom(a,b,c,d):
    return np.matrix([a,c,0],[b,d,0],[0,0,1])

def custom3D(a,b,c,d,e,f):
    return np.matrix([a,c,e,0],[b,d,f,0],[0,0,1])

def transformVertex(titik,matriks):
    return np.mat(titik) * np.mat(matriks)

def transformPolygon(listOfVertex,matriks):
    newList = []
    for v in listOfVertex:
        newList.append(transformVertex(v,matriks))
    return newList
