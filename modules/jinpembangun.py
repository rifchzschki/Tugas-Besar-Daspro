from modules.helper import *
from modules.randomnumber import *
from folder_game.save_1 import *

def cekbahan(pasir, batu, air):
    if pasir >= bahan_bangunan[0][2] or batu >= bahan_bangunan[1][2] or air >= bahan_bangunan[2][2]: 
        return False
    else :
        return True

def bangun():
        if role == "jin_Pembangun":
            p = lcg(1)
            pasir = p[0]
            batu = p[1]        
            air = p[2]
            if cekbahan (pasir, batu, air):
                bahan_bangunan[0][2] = int(bahan_bangunan[0][2]) - pasir           
                bahan_bangunan[1][2] = int(bahan_bangunan[1][2]) - batu
                bahan_bangunan[2][2] = int(bahan_bangunan[2][2]) - air  
                jumlahcandi = 0
                for i in range (100):
                    if candi[i] == None:
                        break
                    else :
                        jumlahcandi += 1

                if jumlahcandi <= 100:
                    candi = candi.append_bikinan(candi, [id, user, pasir, batu, air])
                    print("Candi berhasil dibangun")
                    print (f"Sisa candi yang perlu dibangun: {100-jumlahcandi}")
                else:
                    print ("Candi tidak bisa dibangun.")
                    print("Sisa candi yang perlu dibangun: 0")
            else :
                print ("Bahan bangunan tidak mencukupi.")
                print ("Candi tidak bisa dibangun.")
