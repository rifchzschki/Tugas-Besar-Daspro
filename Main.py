# Fungsi-fungsi minor

def panjang(array) -> int: 
# Menghitung Panjang List
# count : int
    count = 0
    for i in array:
        count +=1
    return count

def split(arr, pemisah) -> list:
# Memisahkan data satu baris menjadi beberapa kolom
# array: list of str
# temp: str
    array = []
    temp = ""
    for i in arr:
        if i == pemisah:
            array.append(temp)
            temp = ""
        else:
            temp += i
    if temp :
        array.append(temp)
    return array
    


def rewrite_csv(csv,file) -> None:
# Mengupdate file
    f = open(f"file/{file}.csv", "w")
    f.write(csv)
    f.close()

def convert_array_csv(array) -> str:
# mengubah array menjadi str berupa csv yang siap upload
# index_baru, i, j, a: int
# arr, data_csv : list of str


    # deklarasi arr 
    index_baru = panjang(array)
    arr = []
    # tambah data baru ke array
    for i in range (index_baru):
        arr += array[i]
    # buat data akhir
    i=-1
    while i < (panjang (arr)-2):
        i += 3 
        arr[i] += "\n"
    for j in range (panjang(arr)):
        a=2
        if j%3 != (2) :
            arr[j] += ";"    
    data_csv = "". join (arr)
    return data_csv

# Fungsi-Fungsi pembantu mayor

# ------------------------------------------------------------Fungsi-Fungsi pembantu mayor------------------------------------------------------------------------------------------
def ambil_data_tanpaKepala()-> list:
# Mengambil data dari user.csv lalu mengolahnya menjadi data yang dapat diakses berupa array

# Kamus Lokal
# raw_lines, lines, raw_header, data, daftar_akun : list of str

    f = open("file/user.csv", "r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    raw_header = lines.pop(0)
    data = []
    for line in lines:
        daftar_akun = split(line, ";")
        data.append(daftar_akun)
    return data

def ambil_data() -> list:
# Mengambil data dari user.csv lalu mengolahnya menjadi data yang dapat diakses berupa array

# Kamus Lokal
# raw_lines, lines, raw_header, data, daftar_akun : list of str

    f = open("file/user.csv", "r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    data = []
    for line in lines:
        daftar_akun = split(line, ";")
        data.append(daftar_akun)
    return data

def cek_username(username: str, data: list) -> bool:
# Mengecek Username

# Kamus Lokal
# benar: bool
    benar = False
    for i in range (panjang(data)):
        for j in range(2):
            if data[i][j] == username:
                benar = True
    return benar

def cek_password(username: str, password: str, data: list) -> bool:
# Mengecek Password

# Kamus Lokal
# benar: bool
# temp: int 
    benar = False
    for i in range(panjang(data)):
        for j in range(2):
            if data[i][j] == username:
                temp = j+1
                if data[i][temp] == password:
                    benar = True
    return benar

def validasi_password(password) -> bool:
# Untuk memastikan bahwa password memenuhi persyaratan
    if panjang(password)<5 or panjang(password)>25:
        return False
    else:
        return True
def masukkan_data_user(username, password, rule) -> None:
# Memasukkan data ke user ke file csv
    # tambah data
    # ambil data lalu ubah ke array
    temp = ambil_data()
    temp.append([username, password, rule])   
    # ubah ke csv
    data = convert_array_csv(temp)
    # simpan ke data user.csv
    rewrite_csv(data,"user")

def cek_maks_jin() -> bool:
# Mengecek jumlah data user
    if panjang(ambil_data_tanpaKepala()) >= 102: #(2 adalah akun bondowoso dengan roro)
        return True
    else:
        return False

# ---------------------------------------------------------Fungsi Utama----------------------------------------------------------------------------------------------
def login() -> None:
# F1: Login
# Login menerima username dan password kemudian akan memunculkan output berupa kebenaran dari data akun

# Kamus Lokal
# username,password : str

# Algoritma
    username = input("Username: ")
    password = input("Password: ")
    print("")
    if cek_username(username,ambil_data_tanpaKepala()):
        if cek_password(username,password,ambil_data_tanpaKepala()):
            print(f"Selamat datang, {username}!")
            print("Masukkan command \"help\" untuk daftar command yang dapat kamu panggil.")
        else:
            print("Password salah!")
    else:
        print("Username tidak terdaftar!")
        

def summonjin() -> None:
# F3: Summon Jin
# Akses Bondowoso dalam memanggil jin, Jin maksimal yang dapat dipanggil adalah 100.

# Kamus Lokal
# sesuai, username_sesuai, password_sesuai: bool
# jenis: int
# jin, password_jin, username_jin: str

# Algoritma
    if cek_maks_jin(): # Mengembalikan nilai True apabila jumlah jin sudah 100
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
                    if not cek_username(username_jin, ambil_data_tanpaKepala()): #jika tidak ada data username di user.csv
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
                                masukkan_data_user(username_jin, password_jin, f"jin_{jin}")
                                print("\nJin Ifrit berhasil dipanggil!")
                            else:
                                print("")
                                print("Password panjangnya harus 5-25 karakter!")
                        
                    else:
                        print(f"\nUsername \"{username_jin}\" sudah diambil!")

            else:
                print(f"\nTidak ada jenis jin bernomor \"{jenis}\"! \n")

def hapusjin() -> None:
# F4: Hilangkan Jin 
# Menghapus Jin, sekaligus menghapus candi yang telah dibuat oleh jin tersebut

# Kamus Lokal
# nama_jin: str
# yakin: char
# data, data_csv:  list of str
# index: int

# Algoritma
    nama_jin = input("Masukkan username jin : ") 
    if not cek_username(nama_jin, ambil_data_tanpaKepala()):
        print("\nTidak ada jin dengan username tersebut.")

    else:
        yakin = input(f"Apakah anda yakin ingin menghapus jin dengan username {nama_jin} (Y/N)? ")
        if yakin == "Y" or yakin == "y":
            data = ambil_data()
            index = panjang(data)
            for i in range(1,index):
                if data[i][0] == nama_jin:
                    data.pop(i)
                    break
            data_csv = convert_array_csv(data)
            rewrite_csv(data_csv,"user")
            
            print("\nJin telah berhasil dihapus dari alam gaib.")
        else:
            print("Oke, Baiklah...")

def ubahjin() -> None:
# F5: Ubah Tipe Jin
# Mengubah tipe jin yang telah tersedia

# Kamus Lokal
# nama_jin, role, nama_role1, nama_role2, data_csv: str
# data: list of str
# kode_role: int
# yakin: char

# Algoritma
    nama_jin = input ("Masukkan username jin : ")
    data = ambil_data()
    if cek_username(nama_jin,ambil_data_tanpaKepala()):
        for i in range(panjang(ambil_data_tanpaKepala())):
            if data[i][0] == nama_jin:
                role = data[i][2]
        if role == "jin_Pembangun":
            kode_role = 0
            nama_role1 = "Pembangun"
            nama_role2 = "Pengumpul"
        elif role == "jin_Pengumpul":
            kode_role = 1
            nama_role1 = "Pengumpul"
            nama_role2 = "Pembangun"
            
        if kode_role == 0:
            yakin = input(f"Jin ini bertipe \"{nama_role1}\". Yakin ingin mengubah ke tipe \"{nama_role2}\" (Y/N)? ")
            if (yakin == "Y") or (yakin == "y"):
                role = "jin_Pengumpul"
    
        elif kode_role == 1:
            yakin = input(f"Jin ini bertipe \"{nama_role1}\". Yakin ingin mengubah ke tipe \"{nama_role2}\" (Y/N)? ")
            if (yakin == "Y") or (yakin == "y"):
                role = "jin_Pembangun"
        
        for i in range(panjang(ambil_data_tanpaKepala())):
            if data[i][0] == nama_jin:
                data[i][2] = role
        data_csv = convert_array_csv(data)
        rewrite_csv(data_csv, "user")
        print("\nJin telah berhasil diubah")
    else:
        print("\nTidak ada jin dengan username tersebut.")


