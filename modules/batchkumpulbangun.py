# F08: Batch Kumpul/Bangun

from modules.randomnumber import *

def jumlah_jin(user:list, role:str) -> int:
# mereturn jumlah jin sesuai role nya

# Kamus Lokal
# count: int

# Algoritma
    count = 0
    for i in range (103):
        if user[i][2] == role:
            count += 1
    return count

def kumpul_bahan(bahan:list) -> list:
# mereturn data bahan bangunan yang telah dikumpulkan

# Kamus Lokal
# p,data_bahan: array of int

# Algoritma
    p = lcg(1)
    data_bahan = [p[0], p[1], p[2]]
    if bahan[1][2] == "none":
        bahan[1] =["pasir", "desc", p[0]]
        bahan[2] =["batu", "desc", p[1]]
        bahan[3] =["air", "desc", p[2]]
    else:
        pasir = int(bahan[1][2]) + p[0]
        batu = int(bahan[2][2]) + p[1]
        air = int(bahan[3][2]) + p[2]
        bahan[1] =["pasir", "desc", pasir]
        bahan[2] =["batu", "desc", batu]
        bahan[3] =["air", "desc", air]
    return data_bahan

def batchkumpul(user: list, bahan: list)-> None:
# Melakukan pengumpulan bahan bangunan dengan perulangan sebanyak total jin pengumpul

# Kamus Lokal
# jumlah, iteration: int
# data_bahan, data_kumpul: array of int

# Algoritma
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

    
def cekbahan(bahan: list, pasir: int, batu: int, air: int)-> bool:
# Proses pengecekan apakah bahan bangunan cukup untuk membangun candi

# Kamus Lokal

# Algoritma
    if pasir > int(bahan[1][2]) or batu > int(bahan[2][2]) or air > int(bahan[3][2]): 
        return False
    else :
        return True
    
def isNone (bahan: list)-> bool:
# Proses pengecekan apakah bahan masih belum dibuat sama sekali

# Kamus Lokal

# Algoritma
    if bahan[1][2] == "none":
        return True
    else:
        return False
    
def isNeg (bil: int)->int:
# Proses memutlakkan bilangan

# Kamus Lokal

# Algoritma
    if bil<0:
        return 0
    else:
        return bil 
    
       

def cekid(candi: list)-> int:
# Proses pengecekan apakah id tersebut belum pernah ada yang pakai

# Kamus Lokal
# found: bool

# Algoritma
    for i in range(1,101):
        found = False
        for j in range(1, 101):
            if candi[j][0] != "none":
                if i == int(candi[j][0]):
                    found = True

        if found == False:
            return i
    
def masukkan_data_candi(pembuat, pasir, batu, air, candi) -> None:   
# Proses memasukkan data candi ke dalam array candi

# Kamus Lokal
# none: bool
# k,index: int

# Algoritma
    none = False  
    k = 0      
    index = cekid(candi)        
    while k<101 and not none:
        if candi[k][0]=="none":
            candi[k] = [index, pembuat, pasir, batu, air]  
            none = True
        k += 1        
       

def cekcandi (candi: list)-> bool:
# Proses pengecekan apakah jumlah candi sudah 100?

# Kamus Lokal
# count: int

# Algoritma
    count = 0
    for i in range (101):
        if candi[i][1] != "none":
            count+=1
    
    if count == 101:
        return True
    else:
        return False

def batchbangun(user: list, bahan: list, candi: list, jumlah_user: int, panjang_candi)-> int:
# Proses membangun candi dengan perulangan sebanyak jumlah jin pembangun

# Kamus Lokal
# i, total_pasir, total_batu, total_air, used_pasir, used_batu, used_air, kurang_pasir, kurang_batu, kurang_air, jumlah: int
# berhasil: bool
# p: array of integer
    if jumlah_jin(user, "jin_pembangun") == 0:
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
    else:
        if not isNone(bahan):
            i = 0
            total_pasir = 0
            total_batu = 0
            total_air = 0
            used_pasir = 0
            used_batu = 0
            used_air = 0
            jumlah = 0
            berhasil = False
            while i < jumlah_user :
                if user[i][2]=="jin_pembangun":
                    p = lcg(1)
                    pasir = p[0]
                    batu = p[1]
                    air = p[2]
                    total_pasir += pasir
                    total_batu += batu
                    total_air += air
                    if cekbahan(bahan, pasir, batu, air):
                        berhasil = True
                        nama_jin = user[i][0]
                        jumlah += 1
                        used_pasir += pasir
                        used_batu += batu
                        used_air += air
                        bahan[1][2] = int(bahan[1][2]) - pasir           
                        bahan[2][2] = int(bahan[2][2]) - batu
                        bahan[3][2] = int(bahan[3][2]) - air  
                        masukkan_data_candi(nama_jin, p[0], p[1], p[2], candi)
                        panjang_candi += 1 
                i += 1
            
            if berhasil:
                print(f"Mengerahkan {jumlah} jin untuk membangun candi dengan total bahan {used_pasir} pasir, {used_batu} batu, dan {used_air} air.")
                print(f"Jin berhasil membangun total {jumlah} candi.")
                print (f"Sisa candi yang perlu dibangun: {101-panjang_candi}")


            else:
                kurang_pasir = total_pasir-int(bahan[1][2])
                kurang_batu = total_batu-int(bahan[2][2])
                kurang_air = total_air-int(bahan[3][2])
                print(f"Bangun gagal. Kurang {isNeg(kurang_pasir)} pasir, {isNeg(kurang_batu)} batu, dan {isNeg(kurang_air)} air.")
            
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
    
                else:
                    p = lcg(1)
                    total_pasir = p[0]
                    total_batu = p[1]
                    total_air = p[2]
                i += 1
                print(f"Bangun gagal. Kurang {total_pasir} pasir, {total_batu} batu, dan {total_air} air.")
    
    return panjang_candi