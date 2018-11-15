import numpy as np
import math


def translate(dx, dy, dz=0):
    return np.mat([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [dx, dy, dz, 1]])


def rotasi(deg, a=0, b=0, c=0):  # degree berlawan arah jarum jam terhadap titik(a,b)
        # normalisasi vektor<a,b,c>
    panjang = np.sqrt(a*a+b*b+c*c)
    if(panjang != 0):
        a /= panjang
        b /= panjang
        c /= panjang
    # normalisasi sudut
    deg = np.deg2rad(deg)
    cosDeg = math.cos(deg)
    sinDeg = math.sin(deg)
    baris1 = [cosDeg+a*a*(1-cosDeg), a*b*(1-cosDeg)-c * sinDeg,
              a*c*(1-cosDeg)+b*sinDeg, 0]
    baris2 = [b*a*(1-cosDeg)+c*sinDeg, cosDeg+b*b * (1-cosDeg),
              b*c*(1-cosDeg)-a*sinDeg, 0]
    baris3 = [c*a*(1-cosDeg)-b*sinDeg, c*b*(1-cosDeg) + a*sinDeg,
              cosDeg+c*c*(1-cosDeg), 0]
    baris4 = [0, 0, 0, 1]
    return np.mat([baris1, baris2, baris3, baris4])
    # return np.mat([math.cos(deg),math.sin(deg),0],[-1*math.sin(deg),math.cos(deg),0],[-1*a*math.cos(deg)+b*math.sin(deg)+m,-1*a*math.sin(deg)-b*math.cos(deg)+n,1])

# asumsi ak make axis Z positif arah keluar layar, negatif masuk ke layar
# rotasi 3D dibawah ini selalu counter-clockwise


def rotasiX(deg):
    # 1 0 0 0
    # 0 cos sin 0
    # 0 -sin cos 0
    # 0 0 0 1
    deg = np.deg2rad(deg)
    return np.mat([[1, 0, 0, 0],
                   [0, math.cos(deg), math.sin(deg), 0],
                   [0, -1*math.sin(deg), math.cos(deg), 0],
                   [0, 0, 0, 1]])


def rotasiY(deg):
    # cos 0 sin 0
    # 0 1 0 0
    # -sin 0 cos 0
    # 0 0 0 1
    deg = np.deg2rad(deg)
    return np.mat([[math.cos(deg), 0, math.sin(deg), 0],
                   [0, 1, 0, 0],
                   [-1*math.sin(deg), 0, math.cos(deg), 0],
                   [0, 0, 0, 1]])


def rotasiZ(deg):
    # cos sin 0 0
    # -sin cos 0 0
    # 0 0 1 0
    # 0 0 0 1
    deg = np.deg2rad(deg)
    return np.mat([[math.cos(deg), math.sin(deg), 0, 0],
                   [-1*math.sin(deg), math.cos(deg), 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])


def dilate(k):
    return np.mat([[k, 0, 0, 0],
                   [0, k, 0, 0],
                   [0, 0, k, 0],
                   [0, 0, 0, 1]])


def reflect(a, b=0):  # a bisa sebagai string atau titik
    if (a == 'x'):
        return np.mat([[1, 0, 0, 0],
                       [0, -1, 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])
    elif (a == 'y'):
        return np.mat([[-1, 0, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])
    elif (a == 'y=x'):
        return np.mat([[0, 1, 0, 0],
                       [1, 0, 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])
    elif (a == 'y=-x'):
        return np.mat([[0, -1, 0, 0],
                       [-1, 0, 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])
    else:  # point (a,b)
        return np.mat([[-1, 0, 0, 0],
                       [0, -1, 0, 0],
                       [2*a, 2*b, 1, 0],
                       [0, 0, 0, 1]])


def reflect3D(s):
    if (s == 'xz'):
        return np.mat([[1, 0, 0, 0],
                       [0, -1, 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])
    elif (s == 'yz'):
        return np.mat([[-1, 0, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])
    elif (s == 'xy'):
        return np.mat([[1, 0, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, -1, 0],
                       [0, 0, 0, 1]])


def shear(param, k):
    if(param == 'x'):
        return np.mat([[1, 0, 0, 0],
                       [k, 1, 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])
    else:  # y
        return np.mat([[1, k, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])


def shear3D(param, k):
    hXY, hXZ, hYX, hYZ, hZX, hZY = [0 for i in range(6)]
    if(param == 'xy'):
        hXY = k
    elif(param == 'xz'):
        hXZ = k
    elif(param == 'yx'):
        hYX = k
    elif(param == 'yz'):
        hYZ = k
    elif(param == 'zx'):
        hZX = k
    elif(param == 'zy'):
        hZY = k
    return np.mat([[1, hYX, hZX, 0],
                   [hXY, 1, hZY, 0],
                   [hXZ, hYZ, 1, 0],
                   [0, 0, 0, 1]])


def stretch(param, k):
    if(param == 'x'):
        return np.mat([[k, 0, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])
    else:  # y
        return np.mat([[1, 0, 0, 0],
                       [0, k, 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])


def stretch3D(param, k):
    if(param == 'x'):  # horizontal
        return np.mat([[k, 0, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])
    elif (param == 'y'):  # vertical
        return np.mat([[1, 0, 0, 0],
                       [0, k, 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])
    elif (param == 'z'):
        return np.mat([[1, 0, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, k, 0],
                       [0, 0, 0, 1]])


def custom(a, b, c, d):
    return np.mat([[a, b, 0, 0],
                   [c, d, 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])


def custom3D(a, b, c, d, e, f, g, h, i):
    return np.mat([[a, b, c, 0],
                   [d, e, f, 0],
                   [g, h, i, 0],
                   [0, 0, 0, 1]])


def transformVertex(titik, matriks):
    return np.mat(titik) * np.mat(matriks)


def transformPolygon(listOfVertex, matriks):
    newList = []
    for v in listOfVertex:
        newList.append(transformVertex(v, matriks))
    return newList
