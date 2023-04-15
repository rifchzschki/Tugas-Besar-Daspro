from modules.helper import *
from modules.load import *
from modules.login import *
from modules.summonjin import *
from modules.hapusjin import *
from modules.ubahjin import *
from modules.exit import *
from modules.help import *
from modules.jinpengumpul import *

import os


load()
# global data_user
# global data_candi
# global data_bahan_bangunan
# (array yang sudah tinggal pakai)
# data_user (kolomnya 3 per baris)
# data_candi (kolomnya 5 per baris)
# data_bahan_bangunan (kolomnya 3 per baris)
user = data_user
candi = data_candi
bahan = data_bahan_bangunan


print ('''
.▄▄ · ▄▄▄ .▄▄▌   ▄▄▄· • ▌ ▄ ·.  ▄▄▄·▄▄▄▄▄    ·▄▄▄▄   ▄▄▄·▄▄▄▄▄ ▄▄▄·  ▐ ▄  ▄▄ • 
▐█ ▀. ▀▄.▀·██•  ▐█ ▀█ ·██ ▐███▪▐█ ▀█•██      ██▪ ██ ▐█ ▀█•██  ▐█ ▀█ •█▌▐█▐█ ▀ ▪
▄▀▀▀█▄▐▀▀▪▄██▪  ▄█▀▀█ ▐█ ▌▐▌▐█·▄█▀▀█ ▐█.▪    ▐█· ▐█▌▄█▀▀█ ▐█.▪▄█▀▀█ ▐█▐▐▌▄█ ▀█▄
▐█▄▪▐█▐█▄▄▌▐█▌▐▌▐█ ▪▐▌██ ██▌▐█▌▐█ ▪▐▌▐█▌·    ██. ██ ▐█ ▪▐▌▐█▌·▐█ ▪▐▌██▐█▌▐█▄▪▐█
 ▀▀▀▀  ▀▀▀ .▀▀▀  ▀  ▀ ▀▀  █▪▀▀▀ ▀  ▀ ▀▀▀     ▀▀▀▀▀•  ▀  ▀ ▀▀▀  ▀  ▀ ▀▀ █▪·▀▀▀▀ 
''')


sudah_login = False
com1 = False

while not com1:
    command = input(">>> ")
    if command == "help":
        help(role)
    elif command == "login" and not sudah_login:
        sudah_login = True
        username = login(user)
        print(username)
        print(user)
        print(role(user, username))
        if role(user, username) == "roro_jonggrang":
            role = role(user, username)
            command_roro = input(">>> ")
            logout = False
            while not logout:
                if command_roro == "help":
                    help(role)
                    command_roro = input(">>> ")
                elif command_roro == "hancurkancandi":
                    # hancurkancandi()
                    
                    ...
                elif command_roro == "ayamberkokok":
                    # ayamberkokok()
                    ...
                elif command_roro == "logout":
                    logout = True
                    sudah_login = False
                elif command_roro == "login" and sudah_login:
                    print(f"Login gagal!\nAnda telah login dengan username {username}, silahkan lakukan \"logout\" sebelum melakukan login kembali.")
                    command_roro = input(">>> ")
                else:
                    help(role)
                    command_roro = input(">>> ")

        elif role(user, username) == "bandung_bondowoso":
            role = role(user, username)
            command_bandung = input(">>> ")
            logout = False
            while not logout:
                if command_bandung == "help":
                    help (role)
                    command_bandung = input(">>> ")
                    ...
                elif command_bandung == "summonjin":
                    summonjin(user) # data user sudah diupdate
                    command_bandung = input(">>> ")
                    ...
                elif command_bandung == "hapusjin":
                    hapusjin(user)
                    command_bandung = input(">>> ")
                    ...
                elif command_bandung == "ubahjin":
                    ubahjin(user)
                    command_bandung = input(">>> ")
                    ...
                elif command_bandung == "batchkumpul":
                    # batchkumpul()
                    ...
                elif command_bandung == "laporanjin":
                    # laporanjin()
                    ...
                elif command_bandung == "laporancandi":
                    # laporancandi()
                    ...
                elif command_bandung == "logout":
                    logout = True
                    sudah_login = False
                elif command_bandung == "login" and sudah_login:
                    print(f"Login gagal!\nAnda telah login dengan username {username}, silahkan lakukan \"logout\" sebelum melakukan login kembali.")
                    command_bandung = input(">>> ")
                else:
                    help(role)
                    command_bandung = input(">>> ")
        elif role(user, username) == "jin_Pembangun":
            role = role(user, username)
            command_jin_pembangun = input(">>> ")
            logout = False
            while not logout:
                if command_jin_pembangun == "help":
                    help(role)
                    command_jin_pembangun = input(">>> ")
                elif command_jin_pembangun == "bangun":
                    # bangun()
                    ...
                elif command_jin_pembangun == "logout":
                    logout = True
                    sudah_login = False
                elif command_jin_pembangun == "login" and sudah_login:
                    print(f"Login gagal!\nAnda telah login dengan username {username}, silahkan lakukan \"logout\" sebelum melakukan login kembali.")
                    command_jin_pembangun = input(">>> ")
                else:
                    help(role)
                    command_jin_pembangun = input(">>> ")
        elif role(user, username) == "jin_Pengumpul":
            role = role(user, username)
            command_jin_pengumpul = input(">>> ")
            logout = False
            while not logout:
                if command_jin_pengumpul == "help":
                    help(role)
                    command_jin_pengumpul = input(">>> ")
                elif command_jin_pengumpul == "kumpul":
                    kumpul()
                    command_jin_pengumpul = input(">>> ")
                    ...
                elif command_jin_pengumpul == "logout":
                    logout = True
                    sudah_login = False
                elif command_jin_pengumpul == "login" and sudah_login:
                    print(f"Login gagal!\nAnda telah login dengan username {username}, silahkan lakukan \"logout\" sebelum melakukan login kembali.")
                    command_jin_pengumpul = input(">>> ")
                else:
                    help(role)
                    command_jin_pengumpul = input(">>> ")
    elif command == "logout":
        print("Logout gagal\nAnda belum login, silahkan login terlebih dahulu untuk melakukan logout.")
    elif command == "exit":
        exit()
        com1 = True
    else:
        role = "none"
        help(role)
        

