# F03: Summon Jin

def cek_username(username: str, user: list) -> bool:
# Mengecek Username

# Kamus Lokal
# benar: bool

# Algoritma
    benar = False
    for i in range (103):
        if user[i][0] == username:
            benar = True
    return benar

def validasi_password(password: str) -> bool:
# Untuk memastikan bahwa password memenuhi persyaratan

# Kamus Lokal

# Algoritma
    if len(password)<5 or len(password)>25:
        return False
    else:
        return True

def masukkan_data_user(username: str, password: str, role: str, user: list) -> None:
# Memasukkan data ke array user

# Kamus Lokal
# i: int
# found: bool

# Algoritma
    i = 0
    found = False
    while i < 103 and not found :
        if user[i][0]== 'none':
            found = True
        if not found:
            i +=1
    user[i] = [username, password, role]          

def summonjin(user: list, panjang: int) -> int:
# Memanggil jin, Jin maksimal yang dapat dipanggil adalah 100.

# Kamus Lokal
# sesuai, username_sesuai, password_sesuai: bool
# jenis: int
# jin, role_jin, password_jin, username_jin: str

# Algoritma
    if panjang >= 103: # Mengembalikan nilai True apabila jumlah jin sudah 100
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
    else:
        print("Jenis jin yang dapat dipanggil:")
        print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print(" (2) Pembangun - Bertugas membangun candi\n")
        sesuai = False
        while not sesuai: #selama nomor jenis belum sesuai
            jenis = input("Masukkan nomor jenis jin yang ingin dipanggil: ")
            if int(jenis) == 1 or int(jenis) == 2:
                if int(jenis) == 1:
                    jin = "Pengumpul"
                    role_jin = "pengumpul"
                else:
                    jin = "Pembangun"
                    role_jin = "pembangun"

                print(f"\nMemilih jin \"{jin}\".")
                username_sesuai = False
                while not username_sesuai:
                    username_jin = input("\nMasukkan username jin: ")
                    if not cek_username(username_jin, user): #jika tidak ada data username di user.csv
                        username_sesuai = True
                        password_sesuai = False
                        while not password_sesuai:
                            password_jin = input("Masukkan password jin: ")
                            if validasi_password(password_jin): #password sudah valid
                                print("")
                                print("Mengumpulkan sesajen...")
                                print("Menyerahkan sesajen...")
                                print("Membacakan mantra...")
                                password_sesuai = True
                                sesuai = True
                                masukkan_data_user(username_jin, password_jin, f"jin_{role_jin}", user)
                                print(f"\nJin {username_jin} berhasil dipanggil!")
                                panjang+=1
                                
                            else:
                                print("")
                                print("Password panjangnya harus 5-25 karakter!")
                        
                    else:
                        print(f"\nUsername \"{username_jin}\" sudah diambil!")

            else:
                print(f"\nTidak ada jenis jin bernomor \"{jenis}\"! \n")

    return panjang
