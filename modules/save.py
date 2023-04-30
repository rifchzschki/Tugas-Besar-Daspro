import os
import time

def rewrite_csv(csv: str, file: str, folder_save) -> None:
# Mengupdate file
    f = open(f"{folder_save}/{file}.csv", "w")
    f.write(csv)
    f.close()


def conv_arr_str(arr: list, nama_arr: str)-> str:
    if nama_arr == "user":
        panjang = 103
        kolom = 3
    elif nama_arr == "candi":
        panjang = 101
        kolom = 5
    else:
        panjang = 4
        kolom = 3

    string = ""
    for i in range (panjang):
        if arr[i][0] != "none":
            for j in range (kolom):
                string += str(arr[i][j])
                if j != (kolom-1):
                    string += ";"
                else:
                    string += "\n"
    return string


def save(user: list, candi: list, bahan: list)-> None:
    folder_save = input("Masukkan nama folder: ")
    print("saving...")
    time.sleep(1)

    user_str = conv_arr_str(user, "user")
    candi_str = conv_arr_str(candi, "candi")
    bahan_str = conv_arr_str(bahan, "bahan")


    if not os.path.isdir("folder_game"):
        os.mkdir("folder_game")
        print("Membuat folder_game ...")
        time.sleep(1)
        os.chdir("folder_game")
        os.mkdir(folder_save)
        print(f"Membuat folder folder_game/{folder_save}...")
        rewrite_csv(user_str, "user", folder_save)
        rewrite_csv(candi_str, "candi", folder_save)
        rewrite_csv(bahan_str, "bahan_bangunan", folder_save)
        print(f"Berhasil menyimpan data di folder folder_game/{folder_save}!")

    else:
        os.chdir("folder_game")
        if not os.path.isdir(folder_save):
            os.mkdir(folder_save)
            print(f"Membuat folder folder_game/{folder_save}...")
            time.sleep(1)

            rewrite_csv(user_str, "user", folder_save)
            rewrite_csv(candi_str, "candi", folder_save)
            rewrite_csv(bahan_str, "bahan_bangunan", folder_save)
            print(f"Berhasil menyimpan data di folder folder_game/{folder_save}!")
        
        else:
            rewrite_csv(user_str, "user", folder_save)
            rewrite_csv(candi_str, "candi", folder_save)
            rewrite_csv(bahan_str, "bahan_bangunan", folder_save)
            print(f"Berhasil menyimpan data di folder folder_game/{folder_save}!")
    os.chdir("../")

