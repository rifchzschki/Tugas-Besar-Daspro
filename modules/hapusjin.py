def cek_username(username: str, data: list, panjang:int) -> bool:
# Mengecek Username

# Kamus Lokal
# benar: bool
    benar = False
    for i in range (panjang):
        if data[i][0] == username:
            benar = True
    return benar

def hapusjin(user, candi, panjang_user, jumlah_candi) -> None:
# F4: Hilangkan Jin 
# Menghapus Jin, sekaligus menghapus candi yang telah dibuat oleh jin tersebut

# Kamus Lokal
# nama_jin: str
# yakin: char
# data, data_csv:  list of str
# index: int

# Algoritma
    nama_jin = input("Masukkan username jin : ") 
    if not cek_username(nama_jin, user, panjang_user):
        print("\nTidak ada jin dengan username tersebut.")

    else:
        yakin = input(f"Apakah anda yakin ingin menghapus jin dengan username {nama_jin} (Y/N)? ")
        if yakin == "Y" or yakin == "y":
            for i in range(103):
                if user[i][0] == nama_jin:
                    user[i] = ["none","none","none"]
                    break
            i=0
            while i<101 :
                if candi[i][1] == nama_jin:
                    candi[i] = ["none","none","none","none","none"]
                    jumlah_candi -= 1
                i+=1
            print("\nJin telah berhasil dihapus dari alam gaib.")
        else:
            print("Oke, Baiklah...")
