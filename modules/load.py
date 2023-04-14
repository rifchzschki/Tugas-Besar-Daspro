import argparse
import os
import time
from modules.helper import *


def load() -> None:
    global data_user
    global data_candi
    global data_bahan_bangunan
    global location

    
    parser = argparse.ArgumentParser(usage="\x1B[3mpython main.py\x1B[0m <nama_folder>")
    parser.add_argument("nama_folder", help="Nama folder game" )

    args = parser.parse_args()

    print("Loading...\n")
    time.sleep(1)
    os.system("cls")
    if os.path.isdir("folder_game") :
        for file in os.listdir("folder_game"):
            if file == args.nama_folder:
                location = f"folder_game/{args.nama_folder}/user.csv"
                data_user = ambil_data(location)
                data_candi = ambil_data(location)
                data_bahan_bangunan = ambil_data(location)
                print("Selamat datang di program \"Manajerial Candi\"")
                break
            elif file == "":
                print("Tidak ada nama folder yang diberikan")
                print(args.help)

            else:
                print(f"Folder \"{args.save_berapa}\" tidak ditemukan.")
                break
load()