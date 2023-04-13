# from modules.helper import *
from modules.load import *
from modules.login import *
import os

load()
# (array yang sudah tinggal pakai)
# data_user (kolomnya 3 per baris)
# data_candi (kolomnya 5 per baris)
# data_bahan_bangunan (kolomnya 3 per baris)
print("Data user", data_user)
print("Data candi", data_candi)
print("Data Bahan Bangunan", data_bahan_bangunan)
os.system('cls')
print ('''
.▄▄ · ▄▄▄ .▄▄▌   ▄▄▄· • ▌ ▄ ·.  ▄▄▄·▄▄▄▄▄    ·▄▄▄▄   ▄▄▄·▄▄▄▄▄ ▄▄▄·  ▐ ▄  ▄▄ • 
▐█ ▀. ▀▄.▀·██•  ▐█ ▀█ ·██ ▐███▪▐█ ▀█•██      ██▪ ██ ▐█ ▀█•██  ▐█ ▀█ •█▌▐█▐█ ▀ ▪
▄▀▀▀█▄▐▀▀▪▄██▪  ▄█▀▀█ ▐█ ▌▐▌▐█·▄█▀▀█ ▐█.▪    ▐█· ▐█▌▄█▀▀█ ▐█.▪▄█▀▀█ ▐█▐▐▌▄█ ▀█▄
▐█▄▪▐█▐█▄▄▌▐█▌▐▌▐█ ▪▐▌██ ██▌▐█▌▐█ ▪▐▌▐█▌·    ██. ██ ▐█ ▪▐▌▐█▌·▐█ ▪▐▌██▐█▌▐█▄▪▐█
 ▀▀▀▀  ▀▀▀ .▀▀▀  ▀  ▀ ▀▀  █▪▀▀▀ ▀  ▀ ▀▀▀     ▀▀▀▀▀•  ▀  ▀ ▀▀▀  ▀  ▀ ▀▀ █▪·▀▀▀▀ 
''')

while True:
    command = input(">>>")
    if command == "login":
        login()

