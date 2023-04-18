import argparse
import os
import time
from modules.helper import *
from modules.inisialisasi_array import *


def load() -> None:
    global data_user
    global data_candi
    global data_bahan
    global panjang_user
    global panjang_candi
    global panjang_bahan

    
    parser = argparse.ArgumentParser(usage="\x1B[3mpython main.py\x1B[0m <nama_folder>")
    parser.add_argument("nama_folder", help="Nama folder game" )

    args = parser.parse_args()

    print("Loading...\n")
    time.sleep(1)
    os.system("cls")
    if os.path.isdir("folder_game") :
        for file in os.listdir("folder_game"):
            if file == args.nama_folder:
                # location = f"folder_game/{args.nama_folder}/user.csv"
                data_user = convert_to_array("user",panjang_file("user"), 3, 103)
                panjang_user = panjang_file("user")
                data_candi = convert_to_array("candi",panjang_file("candi"), 5, 101)
                panjang_candi = panjang_file("candi")
                data_bahan = convert_to_array("bahan_bangunan",panjang_file("bahan_bangunan"), 3, 4)
                panjang_bahan = panjang_file("bahan_bangunan")
                print("Selamat datang di program \"Manajerial Candi\"")
                break
            elif file == "":
                print("Tidak ada nama folder yang diberikan")
                print(args.help)

            else:
                print(f"Folder \"{args.save_berapa}\" tidak ditemukan.")
                break
load()