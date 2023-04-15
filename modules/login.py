from modules.helper import *


def login(user: List) -> str:
# F1: Login
# Login menerima username dan password kemudian akan memunculkan output berupa kebenaran dari data akun

# Kamus Lokal
# username,password : str

# Algoritma
    username = input("Username: ")
    password = input("Password: ")
    username_sudah_benar = False
    while not username_sudah_benar:
        if cek_username(username, user):
            username_sudah_benar = True
            password_sudah_benar = False
            while not password_sudah_benar:
                if cek_password(username,password,user):
                    print(f"\nSelamat datang, {username}!")
                    print("Masukkan command \"help\" untuk daftar command yang dapat kamu panggil.")
                    return username
            
                print("\nPassword salah!\n")
                username = input("Username: ")
                password = input("Password: ")
                password_sudah_benar = True

        
        print("\nUsername tidak terdaftar!\n")
        username = input("Username: ")
        password = input("Password: ")
        username_sudah_benar = False
        

