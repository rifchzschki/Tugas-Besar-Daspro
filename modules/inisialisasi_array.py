def panjang_file(file):
    f = open(f"folder_game/save_1/{file}.csv", "r")
    panjang = 0
    for i in f:
        panjang +=1
    return panjang

def convert_to_array(file, bariseff, kolom, baris_awal):
    arr = [["none" for j in range (kolom)] for i in range (baris_awal)] # baris1, bondo,roro,100 jin
    f = open(f"folder_game/save_1/{file}.csv", "r")
    for i in range(bariseff):
        raw_line = f.readline()
        arr_temp = ["" for i in range(kolom)]
        index = 0
        while index < kolom:
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
    return arr
    
    
