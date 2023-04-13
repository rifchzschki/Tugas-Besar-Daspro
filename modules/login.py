from modules.helper import *

def login() -> None:
# F1: Login
# Login menerima username dan password kemudian akan memunculkan output berupa kebenaran dari data akun

# Kamus Lokal
# username,password : str

# Algoritma
    username = input("Username: ")
    password = input("Password: ")
    print("")
    if cek_username(username,ambil_data_tanpaKepala("file/user.csv")):
        if cek_password(username,password,ambil_data_tanpaKepala("file/user.csv")):
            print(f"Selamat datang, {username}!")
            print("Masukkan command \"help\" untuk daftar command yang dapat kamu panggil.")
        else:
            print("Password salah!")
    else:
        print("Username tidak terdaftar!")

