# from modules.helper import *
from modules.load import *
from modules.login import *
from modules.summonjin import *
from modules.hapusjin import *
from modules.ubahjin import *

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
    command = input("> ")
    if command == "login" and not sudah_login:
        sudah_login = True
        username = login(user)
        logout = False
        if role(user, username) == "roro_jonggrang":
            command_roro = input(">>> ")
            while not logout:
                if command_roro == "hancurkancandi":
                    # hancurkancandi()
                    
                    ...
                elif command_roro == "ayamberkokok":
                    # ayamberkokok()
                    ...
                elif command_roro == "logout":
                    logout = True

        elif role(user, username) == "bandung_bondowoso":
            command_bandung = input(">>> ")
            while not logout:
                if command_bandung == "summonjin":
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
        elif role(user, username) == "jin_pembangun":
            command_jin_pembangun = input(">>> ")
            while not logout:
                if command_jin_pembangun == "bangun":
                    # bangun()
                    ...
                elif command_jin_pembangun == "logout":
                    logout = True
        elif role(user, username) == "jin_pengumpul":
            command_jin_pengumpul = input(">>> ")
            while not logout:
                if command_jin_pengumpul == "kumpul":
                    # kumpul()
                    ...
                elif command_jin_pengumpul == "logout":
                    logout = True
    elif command == "login" and sudah_login:
        print("Login gagal!\nAnda telah login dengan username {username}, silahkan lakukan \"logout\" sebelum melakukan login kembali.")
    elif command == "logout":
        print("Logout gagal\nAnda belum login, silahkan login terlebih dahulu untuk melakukan logout.")
    elif command == "exit":
        # exit()
        com1 = True
        

