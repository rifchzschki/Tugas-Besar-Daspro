from modules.randomnumber import *

def cekbahan(bahan: list, pasir: int, batu: int, air: int)->bool:
    if bahan[1][2] == "none":
        return False
    else:
        if pasir > int(bahan[1][2]) or batu > int(bahan[2][2]) or air > int(bahan[3][2]): 
            return False
        else :
            return True
        

def cekid(candi: list)-> int:
    for i in range(1,101):
        found = False
        for j in range(i, 101):
            if candi[j][0] != "none":
                if i == int(candi[j][0]):
                    found = True

        if found == False:
            return i
    
def masukkan_data_candi(pembuat: str, pasir: int, batu: int, air: int, candi: list) -> None:   
    none = False  
    k = 0      
    index = cekid(candi)        
    while k<101 and not none:
        if candi[k][0]=="none":
            candi[k] = [index, pembuat, pasir, batu, air]  
            none = True
        k += 1        
        

def bangun(username: str, bahan: list, candi: list, jumlah_candi: int)-> int:
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
            jumlah_candi += 1
        else:
            print ("Candi tidak bisa dibangun.")
            print("Sisa candi yang perlu dibangun: 0")
    else :
        print ("Bahan bangunan tidak mencukupi.")
        print ("Candi tidak bisa dibangun.")

    return jumlah_candi