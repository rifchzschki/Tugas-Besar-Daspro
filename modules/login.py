def cek_username(username: str, user: list) -> bool:
# Mengecek Username

# Kamus Lokal
# benar: bool
    benar = False
    for i in range (103):
        if user[i][0] == username:
            benar = True
    return benar

def cek_password(username: str, password: str, data: list) -> bool:
# Mengecek Password

# Kamus Lokal
# benar: bool
# temp: int 
    benar = False
    for i in range(103):
        for j in range(2):
            if data[i][j] == username:
                temp = j+1
                if data[i][temp] == password:
                    benar = True
    return benar


def login(user: list, panjang: int) -> str:
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
        

