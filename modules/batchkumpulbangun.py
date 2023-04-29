from modules.randomnumber import *

def jumlah_jin(user:list, role:str) -> int:
    count = 0
    for i in range (103):
        if user[i][2] == role:
            count += 1
    return count

def kumpul_bahan(bahan:list) -> list:
    p = lcg(1)
    data_bahan = [p[0], p[1], p[2]]
    if bahan[1][2] == "none":
        bahan[1] =["pasir", "desc", data_bahan[0]]
        bahan[2] =["batu", "desc", data_bahan[1]]
        bahan[3] =["air", "desc", data_bahan[2]]
    else:
        pasir = int(bahan[1][2]) + int(data_bahan[0])
        batu = int(bahan[2][2]) + int(data_bahan[1])
        air = int(bahan[3][2]) + int(data_bahan[2])
        bahan[1] =["pasir", "desc", pasir]
        bahan[2] =["batu", "desc", batu]
        bahan[3] =["air", "desc", air]
    return data_bahan

def batchkumpul(user: list, bahan: list)-> None:
    jumlah = jumlah_jin(user, "jin_pengumpul")
    data_bahan = [0,0,0]
    if jumlah == 0 :
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
    else:
        iteration = 0
        print (f"Mengerahkan {jumlah} jin untuk mengumpulkan bahan")
        while iteration < jumlah:
            data_kumpul = kumpul_bahan (bahan)
            data_bahan[0] += data_kumpul[0]
            data_bahan[1] += data_kumpul[1]
            data_bahan[2] += data_kumpul[2]
            iteration += 1
        print(f"Jin menemukan total {data_bahan[0]} pasir, {data_bahan[1]} batu, dan {data_bahan[2]} air.")

    
def cekbahan(bahan: list, pasir: int, batu: int, air: int)->bool:
    if pasir > int(bahan[1][2]) or batu > int(bahan[2][2]) or air > int(bahan[3][2]): 
        return False
    else :
        return True
    
def isNone (bahan: list)->bool:
    if bahan[1][2] == "none":
        return True
    else:
        return False
    
def isNeg (bil: int)->int:
    if bil<0:
        return 0
    else:
        return bil 
    
def masukkan_data_candi(pembuat, pasir, batu, air, candi) -> None:
# Memasukkan data ke user ke file csv
    # tambah data
    # ambil data lalu ubah ke array
    index = 0
    found = False
    while index < 101 and not found :
        if candi[index][0]== 'none':
            found = True
        if not found:
            index +=1
    candi[index] = [index, pembuat, pasir, batu, air]          

def cekcandi (candi: list)->bool:
    count = 0
    for i in range (101):
        if candi[i][1] != "none":
            count+=1
    
    if count == 101:
        return True
    else:
        return False

def batchbangun(user: list, bahan: list, candi: list, jumlah_user: int, panjang_candi: int)->None:
    jumlah = jumlah_jin(user, "jin_pembangun")
    panjang_candi += jumlah
    if jumlah == 0:
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
    else:
        total_pasir = 0
        total_batu = 0
        total_air = 0
        
        i = 0
        while i < jumlah_user :
            if not cekcandi(candi):
                if user[i][2]=="jin_pembangun":
                    p = lcg(1)
                    total_pasir += p[0]
                    total_batu += p[1]        
                    total_air += p[2]
                    nama_jin = user[i][0]
                    masukkan_data_candi(nama_jin, p[0], p[1], p[2], candi) 
            else:
                p = lcg(1)
                total_pasir = p[0]
                total_batu = p[1]
                total_air = p[2]
            i += 1

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

