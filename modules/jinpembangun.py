from modules.randomnumber import *

def cekbahan(bahan, pasir, batu, air):
    if bahan[1][2] == "none":
        return False
    else:
        if pasir > int(bahan[1][2]) or batu > int(bahan[2][2]) or air > int(bahan[3][2]): 
            return False
        else :
            return True
        
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

def bangun(username, bahan, candi, jumlah_candi):
    p = lcg(1)
    pasir = p[0]
    batu = p[1]        
    air = p[2]
    if cekbahan (bahan, pasir, batu, air):
        bahan[1][2] = int(bahan[1][2]) - pasir           
        bahan[2][2] = int(bahan[2][2]) - batu
        bahan[3][2] = int(bahan[3][2]) - air  

        if jumlah_candi <= 100:
            masukkan_data_candi(username, pasir, batu, air, candi)
            print("Candi berhasil dibangun")
            print (f"Sisa candi yang perlu dibangun: {100-jumlah_candi}")
        else:
            print ("Candi tidak bisa dibangun.")
            print("Sisa candi yang perlu dibangun: 0")
    else :
        print ("Bahan bangunan tidak mencukupi.")
        print ("Candi tidak bisa dibangun.")
