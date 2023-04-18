from modules.helper import *

def summonjin(user, panjang) -> None:
# F3: Summon Jin
# Akses Bondowoso dalam memanggil jin, Jin maksimal yang dapat dipanggil adalah 100.

# Kamus Lokal
# sesuai, username_sesuai, password_sesuai: bool
# jenis: int
# jin, password_jin, username_jin: str

# Algoritma
    if panjang >= 103: # Mengembalikan nilai True apabila jumlah jin sudah 100
        print("Jumalah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
    else:
        print("Jenis jin yang dapat dipanggil:")
        print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print(" (2) Pembangun - Bertugas membangun candi\n")
        sesuai = False
        while not sesuai: #selama nomor jenis belum sesuai
            jenis = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
            if jenis == 1 or jenis == 2:
                if jenis == 1:
                    jin = "Pengumpul"
                else:
                    jin = "Pembangun"
                print("")
                print(f"Memilih jin \"{jin}\".")
                username_sesuai = False
                while not username_sesuai:
                    username_jin = input("\nMasukkan username jin: ")
                    if not cek_username(username_jin, user, panjang): #jika tidak ada data username di user.csv
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
                                masukkan_data_user(username_jin, password_jin, f"jin_{jin}", user)
                                print("\nJin Ifrit berhasil dipanggil!")
                                
                            else:
                                print("")
                                print("Password panjangnya harus 5-25 karakter!")
                        
                    else:
                        print(f"\nUsername \"{username_jin}\" sudah diambil!")

            else:
                print(f"\nTidak ada jenis jin bernomor \"{jenis}\"! \n")

