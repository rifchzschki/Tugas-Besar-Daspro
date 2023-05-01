# F11: Hancurkan Candi

def cek_candi(candi: list, hancurkan: int)-> bool:
# Melakukan pengecekan apakah id candi yang ingin dihancurkan ditemukan

# Kamus Lokal
# i: int
# found: bool

# Algoritma
    i = 0
    found = False
    while i < 101 and not found:
        if str(candi[i][0]) == str(hancurkan):
            found = True
        i+=1
    return found        

def hapuscandi(candi: list, idx: int)-> None:
# Melakukan penghapusan (pengubahan data menjadi "none") data pada array candi dengan id sesuai indeks yang ingin dihancurkan

# Kamus Lokal

# Algoritma
    for i in range (1,101):
        if candi[i][0] == idx:
            candi[i] = ["none", "none", "none", "none", "none"]
        
def hancurkancandi(candi: list, panjang_candi: int)-> int:
# Melakukan penghapusan candi sesuai dengan id yang akan dihancurkan

# Kamus Lokal
# hancurkan: int
# YorN: bool
# yakin: str

# Algoritma
    hancurkan = int(input('Masukkan ID candi: '))
    if hancurkan > 100:
        print("Tidak ada candi dengan ID tersebut.") 
    else:
        YorN = False
        if cek_candi(candi, hancurkan):
            while not YorN:
                yakin = input(f'Apakah Anda yakin ingin menghancurkan candi ID: {hancurkan} (Y/N)? ')
                if yakin == 'Y' or yakin=='y':
                    YorN = True
                    for i in range (1,101):
                        if candi[i][0] != "none":
                            if int(candi[i][0]) == hancurkan:
                                candi[i] = ["none", "none", "none", "none", "none"]
                    print(f'Candi ID: {hancurkan} berhasil dihancurkan')
                    panjang_candi -= 1
                elif yakin=='N' or yakin=='n':
                    print(f'Candi ID: {hancurkan} tidak jadi dihancurkan')
                    YorN = True
                else:
                    continue
        else:
            print(f'Tidak ada candi ID: {hancurkan}')
        
        return panjang_candi
