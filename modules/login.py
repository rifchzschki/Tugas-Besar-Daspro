from modules.helper import *


def login(user: List) -> str:
# F1: Login
# Login menerima username dan password kemudian akan memunculkan output berupa kebenaran dari data akun

# Kamus Lokal
# username,password : str

# Algoritma
    while True:
        username = input("Username: ")
        password = input("Password: ")
        print("")
        if cek_username(username, user):
            while  True:
                if cek_password(username,password,user):
                    print(f"Selamat datang, {username}!")
                    print("Masukkan command \"help\" untuk daftar command yang dapat kamu panggil.")
                    return username
                else:
                    print("Password salah!")
        else:
            print("Username tidak terdaftar!")
            break

