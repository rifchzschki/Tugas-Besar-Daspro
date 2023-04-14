from modules.helper import *

def hapusjin(user) -> None:
# F4: Hilangkan Jin 
# Menghapus Jin, sekaligus menghapus candi yang telah dibuat oleh jin tersebut

# Kamus Lokal
# nama_jin: str
# yakin: char
# data, data_csv:  list of str
# index: int

# Algoritma
    nama_jin = input("Masukkan username jin : ") 
    if not cek_username(nama_jin, user):
        print("\nTidak ada jin dengan username tersebut.")

    else:
        yakin = input(f"Apakah anda yakin ingin menghapus jin dengan username {nama_jin} (Y/N)? ")
        if yakin == "Y" or yakin == "y":
            data = user
            index = panjang(data)
            for i in range(1,index):
                if data[i][0] == nama_jin:
                    data.pop(i)
                    break
            user = data
            
            print("\nJin telah berhasil dihapus dari alam gaib.")
        else:
            print("Oke, Baiklah...")
