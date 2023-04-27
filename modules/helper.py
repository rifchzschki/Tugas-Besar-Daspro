# def split(arr: list, pemisah: str) -> list:
# # Memisahkan data satu baris menjadi beberapa kolom
# # array: list of str
# # temp: str
#     array = []
#     temp = ""
#     for i in arr:
#         if i == pemisah:
#             array.append(temp)
#             temp = ""
#         else:
#             temp += i
#     if temp :
#         array.append(temp)
#     return array
    

def cek_username(username: str, data: list, panjang:int) -> bool:
# Mengecek Username

# Kamus Lokal
# benar: bool
    benar = False
    for i in range (panjang):
        if data[i][0] == username:
            benar = True
    return benar

def cek_password(username: str, password: str, data: list, panjang:int) -> bool:
# Mengecek Password

# Kamus Lokal
# benar: bool
# temp: int 
    benar = False
    for i in range(panjang):
        for j in range(2):
            if data[i][j] == username:
                temp = j+1
                if data[i][temp] == password:
                    benar = True
    return benar

# def panjang(string : str)->int:
#     count = 0
#     for i in string:
#         count+=1
#     return count
def validasi_password(password) -> bool:
# Untuk memastikan bahwa password memenuhi persyaratan
    if panjang(password)<5 or panjang(password)>25:
        return False
    else:
        return True
def masukkan_data_user(username, password, role, user) -> None:
# Memasukkan data ke user ke file csv
    # tambah data
    # ambil data lalu ubah ke array
    temp = user
    index = 0
    found = False
    while index < 103 and not found :
        for j in range(3):
            if temp[index][0]== 'none':
                found = True
        if not found:
            index +=1
    temp[index] = [username, password, role]          
    user = temp


    
# p = [[1,2,3],[4,5,6],["none", "none", "none"]]
# print(masukkan_data_user(1,2,3,p,3))
    # # ubah ke csv
    # data = convert_array_csv(temp)
    # # simpan ke data array sementara
    # rewrite_csv(data,"user")

# def cek_maks_jin(user, panjang) -> bool:
# # Mengecek jumlah data user
#     if panjang >= 102: #(2 adalah akun bondowoso dengan roro)
#         return True
#     else:
#         return False

def role_user(user: list, nama_jin: str)-> str:
    data = user
    for i in range(103):
        if data[i][0] == nama_jin:
            jin = data[i][2]
    return jin



def convert_array(raw_array, baris, kolom):
    array = [[() for j in range (kolom)] for i in range (baris)]
    for i in range (baris):
        for j in range (kolom):
            array[i][j] = raw_array[i][j]
    return array

def convert_data_user(data_user):
    arr = [["none" for j in range (3)] for i in range (10)] # baris1, bondo,roro,100 jin
    print(arr)

    print("\n-------------\n")
    f = open(f"folder_game/save_1/user.csv", "r")
    for i in range(8):
        raw_line = f.readline()
        arr_temp = ["" for i in range(3)]
        index = 0
        while index < 3:
            temp = ""
            for j in raw_line:
                
                if j == ";" :
                    arr_temp[index] = temp
                    temp = ""
                    index += 1
                    
                elif j == "\n":
                    arr_temp[index] = temp
                    index += 1 
                
                else:
                    temp += j
        
            arr [i] = arr_temp
    f.close()
    data_user = arr
    




