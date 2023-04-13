import argparse
import os
from modules.helper import *


def load() -> None:
    global data_user
    global data_candi
    global data_bahan_bangunan
    parser = argparse.ArgumentParser()
    parser.add_argument("save_berapa", help="folder save berapa" )

    args = parser.parse_args()

    if os.path.isdir("folder_game") :
        for file in os.listdir(args.folder_game):
            if file == args.save_berapa:
                data_user = ambil_data(f"{args.folder_game}/{args.save_berapa}/user.csv")
                data_candi = ambil_data(f"{args.folder_game}/{args.save_berapa}/candi.csv")
                data_bahan_bangunan = ambil_data(f"{args.folder_game}/{args.save_berapa}/bahan_bangunan.csv")
            elif file == "":
                print("Tidak ada nama folder yang diberikan")
                print(args.help)
            else:
                print(f"Folder \"{args.save_berapa}\" tidak ditemukan.")
load()
