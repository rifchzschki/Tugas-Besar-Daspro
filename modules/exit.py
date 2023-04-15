import os
def exit() -> None:
    yakin = input(f"Apakah Anda mau melakukan penyimpanan file yang sudah diubah (y/n)? ")
    if (yakin == "Y") or (yakin == "y"):
        pass#return ... (save)
    else :
        os._exit(1) #ini function buat terminate program gitu gw pakenya, jadi kalo dia ketik 'n' or 'N' itu bakal auto keluar dari program

