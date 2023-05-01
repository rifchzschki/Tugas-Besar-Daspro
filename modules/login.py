# F1: Login

def cek_username(username: str, data: list, panjang:int) -> bool:
# Mengecek Username

# Kamus Lokal
# benar: bool

# Algoritma
    benar = False
    for i in range (panjang):
        if data[i][0] == username:
            benar = True
    return benar

def cek_password(username: str, password: str, data: list, panjang:int) -> bool:
# Mengecek Password

# Kamus Lokal
# benar: bool
# temp: int

# Algoritma  
    benar = False
    for i in range(panjang):
        for j in range(2):
            if data[i][j] == username:
                temp = j+1
                if data[i][temp] == password:
                    benar = True
    return benar

def login(user: list, panjang: int) -> str:
# Login menerima username dan password kemudian akan memunculkan output berupa kebenaran dari data akun

# Kamus Lokal
# username,password : str
# username_sudah_benar, password_sudah_benar: bool

# Algoritma
    username = input("Username: ")
    password = input("Password: ")
    username_sudah_benar = False
    while not username_sudah_benar:
        if cek_username(username, user , panjang):
            username_sudah_benar = True
            password_sudah_benar = False
            while not password_sudah_benar:
                if cek_password(username,password,user, panjang):
                    print(f"\nSelamat datang, {username}!")
                    print("Masukkan command \"help\" untuk daftar command yang dapat kamu panggil.")
                    return username
                else:
                    print("\nPassword salah!\n")    
                    username = input("Username: ")
                    password = input("Password: ")
                password_sudah_benar = True

        else:
            print("\nUsername tidak terdaftar!\n")
            username = input("Username: ")
            password = input("Password: ")
        username_sudah_benar = False
        

