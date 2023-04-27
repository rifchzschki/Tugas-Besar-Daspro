def cek_username(username: str, data: list, panjang:int) -> bool:
# Mengecek Username

# Kamus Lokal
# benar: bool
    benar = False
    for i in range (panjang):
        if data[i][0] == username:
            benar = True
    return benar

def ubahjin(user, panjang) -> None:
# F5: Ubah Tipe Jin
# Mengubah tipe jin yang telah tersedia

# Kamus Lokal
# nama_jin, role, nama_role1, nama_role2, data_csv: str
# data: list of str
# kode_role: int
# yakin: char

# Algoritma
    nama_jin = input ("Masukkan username jin : ")
    data = user
    if cek_username(nama_jin, user, panjang):
        for i in range(panjang):
            if data[i][0] == nama_jin:
                role = data[i][2]
            
        if role == "jin_pembangun":
            kode_role = 0
            nama_role1 = "Pembangun"
            nama_role2 = "Pengumpul"
        elif role == "jin_pengumpul":
            kode_role = 1
            nama_role1 = "Pengumpul"
            nama_role2 = "Pembangun"
        else:
            kode_role = 3
        
        if kode_role == 0:
            yakin = input(f"Jin ini bertipe \"{nama_role1}\". Yakin ingin mengubah ke tipe \"{nama_role2}\" (Y/N)? ")
            if (yakin == "Y") or (yakin == "y"):
                role = "jin_pengumpul"
                print("\nJin telah berhasil diubah")
    
        elif kode_role == 1:
            yakin = input(f"Jin ini bertipe \"{nama_role1}\". Yakin ingin mengubah ke tipe \"{nama_role2}\" (Y/N)? ")
            if (yakin == "Y") or (yakin == "y"):
                role = "jin_pembangun"
                print("\nJin telah berhasil diubah")
        else:
            print("\nTidak ada jin dengan username tersebut.")
        
        for i in range(panjang):
            if data[i][0] == nama_jin:
                data[i][2] = role
        user = data
        
    else:
        print("\nTidak ada jin dengan username tersebut.")

