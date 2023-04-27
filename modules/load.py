import argparse
import os
import time
from modules.inisialisasi_array import *


def load() -> None:
    global data_user
    global data_candi
    global data_bahan
    global panjang_user
    global panjang_candi
    global panjang_bahan
    
    parser = argparse.ArgumentParser("python3 main.py <nama_folder>")
    parser.add_argument("nama_folder")
    args = parser.parse_args()

    print("Loading...\n")
    time.sleep(1)
    os.system("cls")
    nama_folder = args.nama_folder
    if os.path.isdir("folder_game") :
        found = False
        finish = False
        while not found and not finish:
            for file in os.listdir("folder_game"):
                if file == nama_folder:
                    panjang_user = panjang_file(nama_folder, "user")
                    data_user = convert_to_array(nama_folder, "user", panjang_user, 3, 103)
                    panjang_candi = panjang_file(nama_folder, "candi")
                    data_candi = convert_to_array(nama_folder, "candi", panjang_candi, 5, 101)
                    panjang_bahan = panjang_file(nama_folder, "bahan_bangunan")
                    data_bahan = convert_to_array(nama_folder, "bahan_bangunan", panjang_bahan, 3, 4)
                    print("Selamat datang di program \"Manajerial Candi\"")
                    found = True
            finish = True

        if not found :     
            if nama_folder == "":
                print("Tidak ada nama folder yang diberikan")
                os._exit(0)
                
            else:
                print(f"Folder \"{args.nama_folder}\" tidak ditemukan.")
                os._exit(0)
load()