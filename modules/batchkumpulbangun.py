from modules.randomnumber import *

def jumlah_jin(data, role):
    count = 0
    for i in range (103):
        if data[i][2] == role:
            count += 1
    return count

def kumpul(bahan):
    p = lcg(1)    
    data_bahan = [p[0], p[1], p[2]]
    # print (f"Jin menemukan {data_bahan[0]} pasir, {data_bahan[1]} batu, dan {data_bahan[2]} air.")
    if bahan[1][2] == "none":
        bahan[1] =["pasir", "desc", data_bahan[0]]
        bahan[2] =["batu", "desc", data_bahan[1]]
        bahan[3] =["air", "desc", data_bahan[2]]
    else:
        pasir = bahan[1][2] + data_bahan[0]
        batu = bahan[2][2] + data_bahan[1]
        air = bahan[3][2] + data_bahan[2]
        bahan[1] =["pasir", "desc", pasir]
        bahan[2] =["batu", "desc", batu]
        bahan[3] =["air", "desc", air]
    return data_bahan

def batchkumpul(user, bahan):
    jumlah = jumlah_jin(user, "jin_pengumpul")
    data_bahan = [0,0,0]
    if jumlah == 0 :
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
    else:
        iteration = 0
        print (f"Mengerahkan {jumlah} jin untuk mengumpulkan bahan")
        while iteration < jumlah:
            data_kumpul = kumpul (bahan)
            data_bahan[0] += data_kumpul[0]
            data_bahan[1] += data_kumpul[1]
            data_bahan[2] += data_kumpul[2]
            iteration += 1
        print(f"Jin menemukan total {data_bahan[0]} pasir, {data_bahan[1]} batu, dan {data_bahan[2]} air.")

    
def cekbahan(bahan, pasir, batu, air):

    if pasir > bahan[1][2] or batu > bahan[2][2] or air > bahan[3][2]: 
        return False
    else :
        return True
    
def isNone (bahan):
    if bahan[1][2] == "none":
        return True
    else:
        return False
def isNeg (bil):
    if bil<0:
        return 0
    else:
        return bil 
    
def batchbangun(user, bahan):
    jumlah = jumlah_jin(user, "jin_pembangun")
    if jumlah == 0:
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
    else:
        iteration = 0
        total_pasir = 0
        total_batu = 0
        total_air = 0
        while iteration < jumlah:
            p = lcg(1)
            total_pasir += p[0]
            total_batu += p[1]        
            total_air += p[2]
            iteration += 1
        if isNone(bahan):
            print(f"Bangun gagal. Kurang {total_pasir} pasir, {total_batu} batu, dan {total_air} air.")
        else:
            if cekbahan(bahan, total_pasir, total_batu, total_air):
                bahan[1][2] = int(bahan[1][2]) - total_pasir           
                bahan[2][2] = int(bahan[2][2]) - total_batu
                bahan[3][2] = int(bahan[3][2]) - total_air  
                print(f"Mengerahkan {jumlah} jin untuk membangun candi dengan total bahan {total_pasir} pasir, {total_batu} batu, dan {total_air} air.")
                print(f"Jin berhasil membangun total {jumlah} candi.")
            else:
                kurang_pasir = total_pasir-int(bahan[1][2])
                kurang_batu = total_batu-int(bahan[2][2])
                kurang_air = total_air-int(bahan[3][2])
                print(f"Bangun gagal. Kurang {isNeg(kurang_pasir)} pasir, {isNeg(kurang_batu)} batu, dan {isNeg(kurang_air)} air.")

# cek hitung"ngannya!