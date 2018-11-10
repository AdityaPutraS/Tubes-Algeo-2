from config import config
from transformasi import *

maxKeyFrame = config.maxKeyFrame


def SingleInput(s, is3D):
    if (s[0] == "translate"):
        if (len(s) != 3 and not(is3D)):
            if (len(s) == 4):
                print("Input dx dy dz hanya bisa untuk 3D")
            else:
                print("Input Salah!")
        elif (len(s) != 4 and is3D):
            if (len(s) == 3):
                print("Input dx dy hanya bisa untuk 2D")
            else:
                print("Input Salah!")
        else:
            dx, dy = [float(s[i]) for i in range(1, 3)]
            if (is3D):
                dz = float(s[3])
                print("translasi sebanyak ("+str(dx)+","+str(dy)+","+str(dz)+")")
                config.objTest.animator.startAnimasi(
                    translate(dx/maxKeyFrame, dy/maxKeyFrame, dz/maxKeyFrame))
            else:
                print("translasi sebanyak ("+str(dx)+","+str(dy)+")")
                config.objTest.animator.startAnimasi(translate(dx/maxKeyFrame, dy/maxKeyFrame))
            # fungsi prosedur translate
    elif (s[0] == "rotate"):
        if (len(s) != 4 and not(is3D)):
            if (len(s) == 5):
                print("Input degree dx dy dz hanya bisa untuk 3D")
            else:
                print("Input Salah!")
        elif (len(s) != 5 and is3D):
            if (len(s) == 4):
                print("Input degree dx dy hanya bisa untuk 2D")
            else:
                print("Input Salah!")
        else:
            degree, dx, dy = [float(s[i]) for i in range(1, 4)]
            if (is3D):
                dz = float(s[4])
                print("rotasi sebesar "+str(degree) +
                      " derajat dengan sumbu putar vektor <"+str(dx)+","+str(dy)+","+str(dz)+">")
                config.objTest.animator.startAnimasi(rotasi(degree/maxKeyFrame,dx,dy,dz))
            else:
                print("rotasi sebesar "+str(degree) +
                      " derajat dari pusat ("+str(dx)+","+str(dy)+")")
                config.objTest.animator.startAnimasi(translate(-dx,-dy)*rotasi(degree/maxKeyFrame,0,0,1)*translate(dx,dy))
            # fungsi prosedur rotate
    elif (s[0] == "dilate"):
        if (len(s) != 2):
            print("Input Salah!")
        else:
            ratio = float(s[1])
            print("dilatasi dengan rasio "+str(ratio)+":1")
            config.objTest.animator.startAnimasi(dilate((ratio**(1/maxKeyFrame))))
            # fungsi prosedur dilate
    elif (s[0] == "reflect"):
        if (len(s) != 2):
            print("Input Salah!")
        else:
            param = str(s[1])
            print("refleksi berdasarkan garis "+param)
            # fungsi prosedur reflect
    elif (s[0] == "shear"):
        if (len(s) != 3):
            print("Input Salah!")
        else:
            param = str(s[1])
            k = float(s[2])
            print("shear dgn parameter "+param+" dengan konstanta "+str(k))
            # fungsi prosedur shear
    elif (s[0] == "stretch"):
        if (len(s) != 3):
            print("Input Salah!")
        else:
            param = str(s[1])
            k = float(s[2])
            print("stretch dgn parameter "+param+" dengan konstanta "+str(k))
            # fungsi prosedur stretch
    elif (s[0] == "custom"):
        if (len(s) != 5 and not(is3D)):
            if (len(s) == 10):
                print("Input Matrix 3x3 hanya bisa untuk 3D")
            else:
                print("Input Salah!")
        elif (len(s) != 10 and is3D):
            if (len(s) == 5):
                print("Input Matrix 2x2 hanya bisa untuk 2D")
            else:
                print("Input Salah!")
        else:
            a, b, c, d = [float(s[i]) for i in range(1, 5)]
            if (is3D):
                e, f, g, h, i = [float(s[i]) for i in range(5, 10)]
                print("transformasi custom dengan matrix :")
                print(a, b, c)
                print(d, e, f)
                print(g, h, i)
            else:
                print("transformasi custom dengan matrix :")
                print(a, b)
                print(c, d)
            # fungsi prosedur custom
    elif (s[0] == "reset"):
        config.curMinX, config.curMaxX, config.curMinY, config.curMaxY, config.curMinZ, config.curMaxZ = - \
                10, 10, -10, 10, -10, 10
        config.reset()
    else:
        print("Input salah! Coba Lagi")
    # endif
# end SingleInput procedure


def ProcInput(is3D):
    s = input("$ ").split(" ")
    while (s[0] != "exit"):
        if (s[0] == "multiple"):
            if (len(s) != 2):
                print("Input Salah!")
            else:
                listCommand = []
                for i in range(int(s[1])):
                    print("Perintah ke-"+str(i+1))
                    s2 = input("$ --------- ").split(" ")
                    if ((s2[0] != "exit") and (s2[0] != "exitmultiple")):
                        listCommand.append(s2)
                    else:
                        break
                    # endif
                # endforloop
                for command in listCommand:
                    SingleInput(command,is3D)
                print("Keluar dari perintah multiple")
            # endif
        else:
            SingleInput(s, is3D)
        # endif
        s = input("$ ").split(" ")
    # endwhile
    config.jalan = False
# end ProcInput procedure
