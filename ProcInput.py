def SingleInput(s, is3D):
    if (s[0] == "translate"):
        dx,dy = [float(s[i]) for i in range(1,3)]
        if (is3D):
            dz = float(s[3])
            print("translasi sebanyak ("+str(dx)+","+str(dy)+","+str(dz)+")")
        else :
            print("translasi sebanyak ("+str(dx)+","+str(dy)+")")
        # fungsi prosedur translate
    elif (s[0] == "rotate"):
        degree,dx,dy = [float(s[i]) for i in range(1,4)]
        if (is3D):
            dz = float(s[4])
            print("rotasi sebesar "+str(degree)+" derajat dari pusat ("+str(dx)+","+str(dy)+","+str(dz)+")")
        else :
            print("rotasi sebesar "+str(degree)+" derajat dari pusat ("+str(dx)+","+str(dy)+")")
        # fungsi prosedur rotate
    elif (s[0] == "dilate"):
        ratio = float(s[1])
        print("dilatasi dengan rasio "+str(ratio))
        # fungsi prosedur dilate
    elif (s[0] == "reflect"):
        param = str(s[1])
        print("refleksi berdasarkan garis "+param)
        # fungsi prosedur reflect
    elif (s[0] == "shear"):
        param = str(s[1])
        k = float(s[2])
        print("shear dgn parameter "+param+" dengan konstanta "+str(k))
        # fungsi prosedur shear
    elif (s[0] == "stretch"):
        param = str(s[1])
        k = float(s[2])
        print("stretch dgn parameter "+param+" dengan konstanta "+str(k))
        # fungsi prosedur shear
    elif (s[0] == "custom"):
        #baru untuk 2D
        a,b,c,d = [float(s[i]) for i in range(1,5)]
        if (is3D):
            e,f,g,h,i = [float(s[i]) for i in range(5,10)]
            print("transformasi custom dengan matrix :")
            print(a,b,c)
            print(d,e,f)
            print(g,h,i)
        else :
            print("transformasi custom dengan matrix :")
            print(a,b)
            print(c,d)
        # fungsi prosedur custom
    else :
        print("Input salah! Coba Lagi")
    #endif
#end SingleInput procedure

def ProcInput(is3D):
    s = input().split(" ")
    while (s[0] != "exit"):
        if (s[0] == "multiple"):
            for i in range(int(s[1])):
                print("ini perintah ke-"+str(i+1))
                s2 = input().split(" ")
                if ((s2[0] != "exit") and (s2[0] != "exitmultiple")):
                    SingleInput(s2, is3D)
                else :
                    print("keluar dari multiple")
                    break
                #endif
            #endforloop
        else :
            SingleInput(s, is3D)
        #endif
        s = input().split(" ")
    #endwhile
#end ProcInput procedure

#mainprogram
if __name__ == "__main__" :
    stis3D = input("Apakah anda ingin melakukan transformasi 3D?(Y = Yes, N = No) ")
    ProcInput((stis3D == 'Y') or (stis3D == 'y'))
#endmainprogram

#ini cuma program untuk baca inputan doang
