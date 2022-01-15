def nama(): 
    global nm
    nm =  input('masukan nama\t\t: ')
    return nm

def nim():
    global n
    n = input('masukan nim\t\t: ')
    return n

def tugas():
    global tgs
    tgs = int(input('masukan nilai tugas\t: '))
    return tgs

def uts():
    global ut
    ut = int(input('masukan nilai uts\t: '))
    return ut

def uas():
    global ua
    ua = int(input('masukan nilai uas\t: '))
    return ua

def akhir():
    global ak
    ak = (0.30*tgs)+(0.35*ut)+(0.35*ua)
    return ak
