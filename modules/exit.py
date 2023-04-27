import os
from modules.save import *

def exit(user, candi, bahan) -> None:
    yakin = input(f"Apakah Anda mau melakukan penyimpanan file yang sudah diubah (y/n)? ")
    if (yakin == "Y") or (yakin == "y"):
        save(user,candi,bahan)
        os._exit(0)
    else :
        os._exit(0) 