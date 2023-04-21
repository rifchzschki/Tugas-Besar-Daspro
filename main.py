from modules.helper import *
from modules.load import *
from modules.login import *
from modules.summonjin import *
from modules.hapusjin import *
from modules.ubahjin import *
from modules.exit import *
from modules.help import *
from modules.jinpengumpul import *
from modules.jinpembangun import *
from modules.hancurkancandi import *
from modules.ayamberkokok import *
from modules.batchkumpulbangun import *
from modules.save import *


import os


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

# print(user)
# print(bahan)

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
                    hancurkancandi(candi)
                    command_roro = input(">>> ")
                    ...
                elif command_roro == "ayamberkokok":
                    ayamberkokok(panjang_candi)
                elif command_roro == "save":
                    save(user, candi, bahan)
                    command_roro = input(">>> ")
                elif command_roro == "logout":
                    logout = True
                    sudah_login = False
                    
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
                    ...
                elif command_bandung == "summonjin":
                    summonjin(user, panjang_user) # data user sudah diupdate
                    panjang_user +=1
                    command_bandung = input(">>> ")
                    ...
                elif command_bandung == "hapusjin":
                    hapusjin(user, panjang_user)
                    panjang_user -=1
                    command_bandung = input(">>> ")
                    ...
                elif command_bandung == "ubahjin":
                    ubahjin(user, panjang_user)
                    command_bandung = input(">>> ")
                    ...
                elif command_bandung == "batchkumpul":
                    batchkumpul(user, bahan)
                    # print(bahan)
                    command_bandung = input (">>> ")
                    ...
                elif command_bandung == "batchbangun":
                    batchbangun(user, bahan)
                    # print(bahan)
                    command_bandung = input (">>> ")
                    ...
                elif command_bandung == "laporanjin":
                    # laporanjin()
                    ...
                elif command_bandung == "laporancandi":
                    # laporancandi()
                    ...
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
                    bangun(username, bahan, candi, panjang_candi)
                    command_jin_pembangun = input(">>> ")
                elif command_jin_pembangun == "logout":
                    logout = True
                    sudah_login = False
                elif command_jin_pembangun == "save":
                    save(user, candi, bahan)
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
                    ...
                elif command_jin_pengumpul == "logout":
                    logout = True
                    sudah_login = False
                elif command_jin_pengumpul == "save":
                    save(user, candi, bahan)
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
        

