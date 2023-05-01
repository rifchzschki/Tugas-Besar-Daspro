# Program Utama

from modules.load import *
from modules.login import *
from modules.summonjin import *
from modules.hapusjin import *
from modules.ubahjin import *
from modules.exit import *
from modules.help import *
from modules.laporanjin import *
from modules.laporancandi import *
from modules.jinpengumpul import *
from modules.jinpembangun import *
from modules.hancurkancandi import *
from modules.ayamberkokok import *
from modules.batchkumpulbangun import *
from modules.save import *
import os

# Kamus
# user, candi, bahan: array of any
# sudah_login, logout com1: bool
# command, command_bandung, command_roro, command_jin_pembangun, command_jin_pengumpul, role: str

# Algoritma
def role_user(user: list, nama_jin: str)-> str:
# Menentukan role dari user

# Kamus Lokal
# jin: str
    
# Algoritma
    for i in range(103):
        if user[i][0] == nama_jin:
            jin = user[i][2]
    return jin

load()

# (array yang sudah tinggal pakai)
# data_user (kolomnya 3 per baris)
# data_candi (kolomnya 5 per baris)
# data_bahan_bangunan (kolomnya 3 per baris)
# panjang_user_max = 103
# panjang_candi_max = 101 

user = data_user
candi = data_candi
bahan = data_bahan



print ('''
.▄▄ · ▄▄▄ .▄▄▌   ▄▄▄· • ▌ ▄ ·.  ▄▄▄·▄▄▄▄▄    ·▄▄▄▄   ▄▄▄·▄▄▄▄▄ ▄▄▄·  ▐ ▄  ▄▄ • 
▐█ ▀. ▀▄.▀·██•  ▐█ ▀█ ·██ ▐███▪▐█ ▀█•██      ██▪ ██ ▐█ ▀█•██  ▐█ ▀█ •█▌▐█▐█ ▀ ▪
▄▀▀▀█▄▐▀▀▪▄██▪  ▄█▀▀█ ▐█ ▌▐▌▐█·▄█▀▀█ ▐█.▪    ▐█· ▐█▌▄█▀▀█ ▐█.▪▄█▀▀█ ▐█▐▐▌▄█ ▀█▄
▐█▄▪▐█▐█▄▄▌▐█▌▐▌▐█ ▪▐▌██ ██▌▐█▌▐█ ▪▐▌▐█▌·    ██. ██ ▐█ ▪▐▌▐█▌·▐█ ▪▐▌██▐█▌▐█▄▪▐█
 ▀▀▀▀  ▀▀▀ .▀▀▀  ▀  ▀ ▀▀  █▪▀▀▀ ▀  ▀ ▀▀▀     ▀▀▀▀▀•  ▀  ▀ ▀▀▀  ▀  ▀ ▀▀ █▪·▀▀▀▀ 
''')
print("Type any character for help")

sudah_login = False
com1 = False

while not com1:
    command = input(">>> ")
    if command == "help":
        role = "none"
        help(role)
    elif command == "login" and not sudah_login:
        sudah_login = True
        username = login(user, panjang_user)
        if role_user(user, username) == "roro_jonggrang":
            role = role_user(user, username)
            command_roro = input(">>> ")
            logout = False
            while not logout:
                if command_roro == "help":
                    help(role)
                    command_roro = input(">>> ")
                elif command_roro == "hancurkancandi":
                    panjang_candi = hancurkancandi(candi, panjang_candi)
                    command_roro = input(">>> ")
                elif command_roro == "ayamberkokok":
                    ayamberkokok(panjang_candi)
                elif command_roro == "save":
                    save(user, candi, bahan)
                    command_roro = input(">>> ")
                elif command_roro == "logout":
                    logout = True
                    sudah_login = False
                elif command_roro == "laporancandi":
                    print("Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso.")
                    command_roro = input(">>> ")
                elif command_roro == "laporanjin":
                    print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
                    command_roro = input(">>> ")
                elif command_roro == "login" and sudah_login:
                    print(f"Login gagal!\nAnda telah login dengan username {username}, silahkan lakukan \"logout\" sebelum melakukan login kembali.")
                    command_roro = input(">>> ")
                else:
                    help(role)
                    command_roro = input(">>> ")

        elif role_user(user, username) == "bandung_bondowoso":
            role = role_user(user, username)
            command_bandung = input(">>> ")
            logout = False
            while not logout:
                if command_bandung == "help":
                    help (role)
                    command_bandung = input(">>> ")
                elif command_bandung == "summonjin":
                    panjang_user = summonjin(user, panjang_user)
                    command_bandung = input(">>> ")
                elif command_bandung == "hapusjin":
                    data = hapusjin(user, candi, panjang_candi, panjang_user)
                    panjang_user = data[0]
                    panjang_candi = data[1]
                    command_bandung = input(">>> ")
                elif command_bandung == "ubahjin":
                    ubahjin(user, panjang_user)
                    command_bandung = input(">>> ")
                elif command_bandung == "batchkumpul":
                    batchkumpul(user, bahan)
                    command_bandung = input (">>> ")
                elif command_bandung == "batchbangun":
                    panjang_candi = batchbangun(user, bahan, candi, panjang_user, panjang_candi)
                    command_bandung = input (">>> ")
                elif command_bandung == "laporanjin":
                    laporanjin(user, candi, bahan)
                    command_bandung = input (">>> ")
                elif command_bandung == "laporancandi":
                    laporancandi(candi , panjang_candi)
                    command_bandung = input(">>> ")
                elif command_bandung == "save":
                    save(user, candi, bahan)
                    command_bandung = input(">>> ")
                elif command_bandung == "logout":
                    logout = True
                    sudah_login = False
                elif command_bandung == "login" and sudah_login:
                    print(f"Login gagal!\nAnda telah login dengan username {username}, silahkan lakukan \"logout\" sebelum melakukan login kembali.")
                    command_bandung = input(">>> ")
                else:
                    help(role)
                    command_bandung = input(">>> ")
        elif role_user(user, username) == "jin_pembangun":
            role = role_user(user, username)
            command_jin_pembangun = input(">>> ")
            logout = False
            while not logout:
                if command_jin_pembangun == "help":
                    help(role)
                    command_jin_pembangun = input(">>> ")
                elif command_jin_pembangun == "bangun":
                    panjang_candi = bangun(username, bahan, candi, panjang_candi)
                    command_jin_pembangun = input(">>> ")
                elif command_jin_pembangun == "logout":
                    logout = True
                    sudah_login = False
                elif command_jin_pembangun == "save":
                    save(user, candi, bahan)
                    command_jin_pembangun = input(">>> ")
                elif command_jin_pembangun == "laporanjin":
                    print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
                    command_jin_pembangun = input(">>> ")
                elif command_jin_pembangun == "laporancandi":
                    print("Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso.")
                    command_jin_pembangun = input(">>> ")
                elif command_jin_pembangun == "login" and sudah_login:
                    print(f"Login gagal!\nAnda telah login dengan username {username}, silahkan lakukan \"logout\" sebelum melakukan login kembali.")
                    command_jin_pembangun = input(">>> ")
                else:
                    help(role)
                    command_jin_pembangun = input(">>> ")
        elif role_user(user, username) == "jin_pengumpul":
            role = role_user(user, username)
            command_jin_pengumpul = input(">>> ")
            logout = False
            while not logout:
                if command_jin_pengumpul == "help":
                    help(role)
                    command_jin_pengumpul = input(">>> ")
                elif command_jin_pengumpul == "kumpul":
                    kumpul(bahan)
                    command_jin_pengumpul = input(">>> ")
                elif command_jin_pengumpul == "logout":
                    logout = True
                    sudah_login = False
                elif command_jin_pengumpul == "save":
                    save(user, candi, bahan)
                    command_jin_pengumpul = input(">>> ")
                elif command_jin_pengumpul == "laporanjin":
                    print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
                    command_jin_pengumpul = input(">>> ")
                elif command_jin_pengumpul == "laporancandi":
                    print("Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso.")
                    command_jin_pengumpul = input(">>> ")
                elif command_jin_pengumpul == "login" and sudah_login:
                    print(f"Login gagal!\nAnda telah login dengan username {username}, silahkan lakukan \"logout\" sebelum melakukan login kembali.")
                    command_jin_pengumpul = input(">>> ")
                else:
                    help(role)
                    command_jin_pengumpul = input(">>> ")
    elif command == "logout":
        print("Logout gagal\nAnda belum login, silahkan login terlebih dahulu untuk melakukan logout.")
    elif command == "exit":
        exit(user, candi, bahan)
        com1 = True
    else:
        role = "none"
        help(role)
        

