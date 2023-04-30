
# ord(char)
# a=97, z=122
# A=65, Z=90
def totaljin(user, role):
    count = 0
    for i in range (101):
        if user[i][2] == role:
            count +=1
    return count

def cekleksikal(string1, string2, predikat):
    panjang1 = len(string1)
    panjang2 = len(string2)

    if panjang1>=panjang2:
        indeks = 0
        masih_sama = True
        while indeks<panjang2:
            if ord(string1[indeks])>ord(string2[indeks]):
                masih_sama = False
                if predikat == "rajin":
                    return string2
                else:
                    return string1
            elif ord(string1[indeks])<ord(string2[indeks]) :
                masih_sama = False
                if predikat == "rajin":
                    return string1
                else:
                    return string2
            else:
                indeks += 1
        if masih_sama == True:
            if predikat == "rajin":
                return string2
            else:
                return string1
        
    else:
        indeks = 0
        masih_sama = True
        while indeks<panjang1:
            if ord(string1[indeks])>ord(string2[indeks]):
                masih_sama = False
                if predikat == "rajin":
                    return string2
                else:
                    return string1
            elif ord(string1[indeks])<ord(string2[indeks]) :
                masih_sama = False
                if predikat == "rajin":
                    return string1
                else:
                    return string2
            else:
                indeks += 1

        if masih_sama == True:
            if predikat == "rajin":
                return string1
            else:
                return string2
print(cekleksikal("unta","eqee","malas"))

def laporanjin(user, candi, bahan):
    total_jin_pengumpul = totaljin(user, "jin_pengumpul")
    total_jin_pembangun = totaljin(user, "jin_pembangun")
    total_jin = total_jin_pengumpul + total_jin_pembangun

    pembuat_candi = [["", 0]for i in range(101)]
    jumlah_pembuat = 0
    for i in range (3,103):
        if user[i][0] != "none":
            pembuat_candi [jumlah_pembuat][0] = user[i][0]
            jumlah_pembuat += 1
            
    
    for i in range (jumlah_pembuat):
        jumlah = 0
        for j in range(1,101):
            if pembuat_candi[i][0] == candi[j][1]:
                jumlah += 1
        pembuat_candi[i][1] = jumlah

    terajin = ["", 0]
    n = terajin[1]
    name = terajin[0]
    for i in range (jumlah_pembuat):
        if pembuat_candi[i][0] != "":
            if int(pembuat_candi[i][1]) >= n:
                if int(pembuat_candi[i][1]) > n:
                    n = pembuat_candi[i][1]
                    name = pembuat_candi[i][0]
                else:
                    name = cekleksikal(name, pembuat_candi[i][0], "rajin")
    jin_terajin = name

    termalas = ["", 999]
    n = termalas[1]
    name = termalas[0]
    for i in range (jumlah_pembuat):
        if pembuat_candi[i][0] != "":
            if int(pembuat_candi[i][1]) <= n:
                if int(pembuat_candi[i][1]) < n:
                    n = pembuat_candi[i][1]
                    name = pembuat_candi[i][0]
                else:
                    name = cekleksikal(name ,pembuat_candi[i][0], "malas")
    jin_termalas = name

    if bahan[1][0] == "none":
        pasir = 0
        batu = 0
        air = 0
    else:
        pasir = bahan[1][2]
        batu = bahan[2][2]
        air = bahan[3][2]

    print(f"\n> Total Jin: {total_jin}")
    print(f"> Total Jin Pengumpul: {total_jin_pengumpul}")
    print(f"> Total Jin Pembangun: {total_jin_pembangun}")
    print(f"> Jin Terajin: {jin_terajin}")
    print(f"> Jin Termalas: {jin_termalas}")
    print(f"> Jumlah Pasir: {pasir} unit")
    print(f"> Jumlah Batu: {batu} unit")
    print(f"> Jumlah Air: {air} unit")
    