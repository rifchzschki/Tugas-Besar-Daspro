# Fungsi-fungsi minor
from typing import *

def panjang(array: List) -> int: 
# Menghitung Panjang List
# count : int
    count = 0
    while array[count:]:
        count +=1
    return count


def split(arr: List, pemisah: str) -> list:
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
    


def rewrite_csv(csv: str, file: str) -> None:
# Mengupdate file
    f = open(f"file/{file}.csv", "w")
    f.write(csv)
    f.close()

def convert_array_csv(array: list) -> str:
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
def ambil_data_tanpaKepala(loc: str )-> list:
# Mengambil data dari user.csv lalu mengolahnya menjadi data yang dapat diakses berupa array

# Kamus Lokal
# raw_lines, lines, raw_header, data, daftar_akun : list of str

    f = open(f"{loc}", "r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    raw_header = lines.pop(0)
    data = []
    for line in lines:
        daftar_akun = split(line, ";")
        data.append(daftar_akun)
    return data

def ambil_data(loc) -> list:
# Mengambil data dari user.csv lalu mengolahnya menjadi data yang dapat diakses berupa array

# Kamus Lokal
# raw_lines, lines, raw_header, data, daftar_akun : list of str

    f = open(f"{loc}", "r")
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
def masukkan_data_user(username, password, rule, user) -> None:
# Memasukkan data ke user ke file csv
    # tambah data
    # ambil data lalu ubah ke array
    temp = user
    temp.append([username, password, rule])   
    user = temp
    # # ubah ke csv
    # data = convert_array_csv(temp)
    # # simpan ke data array sementara
    # rewrite_csv(data,"user")

def cek_maks_jin(user) -> bool:
# Mengecek jumlah data user
    if panjang(user) >= 102: #(2 adalah akun bondowoso dengan roro)
        return True
    else:
        return False

def role_user(user: List, nama_jin: str)-> str:
    data = user
    for i in range(panjang(user)):
        if data[i][0] == nama_jin:
            jin = data[i][2]
    return jin

# print(role([["a","b","c"],["d","e","f"]], "d"))