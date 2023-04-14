import os
def exit() -> None:
    yakin = input(f"Apakah Anda mau melakukan penyimpanan file yang sudah diubah (y/n)? ")
    if (yakin == "Y") or (yakin == "y"):
        pass#return ... (save)
    else :
        os._exit(1)

