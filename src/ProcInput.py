from config import config
from transformasi import *
from OpenGL.GLUT import glutLeaveMainLoop
maxKeyFrame = config.maxKeyFrame


def SingleInput(s, is3D):
    if (s[0] == "translate"):
        if (len(s) != 3 and not(is3D)):
            if (len(s) == 4):
                print("Input dx dy dz hanya bisa untuk 3D")
            else:
                print("Input salah!")
        elif (len(s) != 4 and is3D):
            if (len(s) == 3):
                print("Input dx dy hanya bisa untuk 2D")
            else:
                print("Input salah!")
        else:
            dx, dy = [float(s[i]) for i in range(1, 3)]
            if (is3D):
                dz = float(s[3])
                print("translasi sebanyak ("+str(dx)+","+str(dy)+","+str(dz)+")")
                config.objTest.animator.pushAnimasi(
                    [translate(dx/maxKeyFrame, dy/maxKeyFrame, dz/maxKeyFrame),False])
            else:
                print("translasi sebanyak ("+str(dx)+","+str(dy)+")")
                config.objTest.animator.pushAnimasi([translate(dx/maxKeyFrame, dy/maxKeyFrame),False])
            # fungsi prosedur translate
    elif (s[0] == "rotate"):
        if (len(s) != 4 and not(is3D)):
            if (len(s) == 5):
                print("Input degree <x, y, z> hanya bisa untuk 3D")
            else:
                print("Input salah!")
        elif (len(s) != 5 and is3D):
            if (len(s) == 4):
                print("Input degree <x, y> hanya bisa untuk 2D")
            else:
                print("Input salah!")
        else:
            degree, dx, dy = [float(s[i]) for i in range(1, 4)]
            if (is3D):
                dz = float(s[4])
                print("rotasi sebesar "+str(degree) +
                      " derajat dengan sumbu putar vektor <"+str(dx)+","+str(dy)+","+str(dz)+">")
                config.objTest.animator.pushAnimasi([rotasi(-degree/maxKeyFrame,dx,dy,dz),False])
            else:
                print("rotasi sebesar "+str(degree) +
                      " derajat dari pusat ("+str(dx)+","+str(dy)+")")
                config.objTest.animator.pushAnimasi([translate(-dx,-dy)*rotasi(-degree/maxKeyFrame,0,0,1)*translate(dx,dy),False])
            # fungsi prosedur rotate
    elif (s[0] == "dilate"):
        if (len(s) != 2):
            print("Input salah!")
        else:
            ratio = float(s[1])
            if(ratio > 0):
                print("dilatasi dengan rasio "+str(ratio)+":1")
                config.objTest.animator.pushAnimasi([dilate((ratio**(1/maxKeyFrame))),False])
            else:
                print("Input salah! (rasio harus > 0)")
    elif (s[0] == "reflect"):
        if (len(s) != 2 and len(s) != 3):
            print("Input salah!")
        else:
            param = s[1]
            if(len(s) == 3):
                #Refleksi terhadap titik (a,b)
                param = int(param)
                param2 = int(s[2])
                print("refleksi berdasarkan titik ("+s[1]+","+s[2]+")")
                config.objTest.animator.pushAnimasi([reflect(param,param2),True])
            else:
                print("refleksi berdasarkan garis "+param)
                if(is3D):
                    config.objTest.animator.pushAnimasi([reflect3D(param),True])
                else:
                    config.objTest.animator.pushAnimasi([reflect(param),True])
            # fungsi prosedur reflect
    elif (s[0] == "shear"):
        if (len(s) != 3):
            print("Input salah!")
        else:
            param = s[1]
            k = float(s[2])
            print("shear dgn parameter "+param+" dengan konstanta "+str(k))
            if(config.is3D):
                config.objTest.animator.pushAnimasi([shear3D(param,k/maxKeyFrame),False])
            else:
                config.objTest.animator.pushAnimasi([shear(param,k/maxKeyFrame),False])
    elif (s[0] == "stretch"):
        if (len(s) != 3):
            print("Input salah!")
        else:   
            param = str(s[1])
            k = float(s[2])
            if(k >= 0):
                print("stretch dgn parameter "+param+" dengan konstanta "+str(k))
                if(config.is3D):
                    config.objTest.animator.pushAnimasi([stretch3D(param,k**(1/maxKeyFrame)),False])
                else:
                    config.objTest.animator.pushAnimasi([stretch(param,k**(1/maxKeyFrame)),False])
            else:
                print("Input salah! konstanta harus >= 0")
    elif (s[0] == "custom"):
        if (len(s) != 5 and not(is3D)):
            if (len(s) == 10):
                print("Input Matrix 3x3 hanya bisa untuk 3D")
            else:
                print("Input salah!")
        elif (len(s) != 10 and is3D):
            if (len(s) == 5):
                print("Input Matrix 2x2 hanya bisa untuk 2D")
            else:
                print("Input salah!")
        else:
            a, b, c, d = [float(s[i]) for i in range(1, 5)]
            if (is3D):
                e, f, g, h, i = [float(s[i]) for i in range(5, 10)]
                print("transformasi custom dengan matrix :")
                print(a, b, c)
                print(d, e, f)
                print(g, h, i)
                config.objTest.animator.pushAnimasi([custom3D(a,b,c,d,e,f,g,h,i),True])
            else:
                print("transformasi custom dengan matrix :")
                print(a, b)
                print(c, d)
                config.objTest.animator.pushAnimasi([custom(a,b,c,d),True])
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
    if(not(is3D)):
        #Baca koordinat 2d
        banyakKoordinat = int(input("Banyak koordinat 2D : "))
        listVertexInput = []
        for i in range(banyakKoordinat):
            inp = input("Koordinat "+str(i)+" : ").split(" ")
            listVertexInput.append(np.mat([[float(inp[0]),float(inp[1]),0,1]]))
        config.initAwal(is3D,listVertexInput,False)
    s = input("$ ").split(" ")
    while (s[0] != "exit"):
        if (s[0] == "multiple"):
            if (len(s) != 2):
                print("Input salah!")
            else:
                listCommand = []
                lanjut = True
                i = 0
                while(i < int(s[1]) and lanjut):
                    print("Perintah ke-"+str(i+1))
                    s2 = input("$ --------- ").split(" ")
                    if ((s2[0] != "exit") and (s2[0] != "exitmultiple")):
                        if(s2[0] != "reset"):
                            listCommand.append(s2)
                            i += 1
                        else:
                            print("Tidak bisa melakukan reset didalam multiple")
                    else:
                        lanjut = False
                    # endif
                # endforloop
                if ((s2[0] != "exit") and (s2[0] != "exitmultiple")):
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
    glutLeaveMainLoop()
# end ProcInput procedure
