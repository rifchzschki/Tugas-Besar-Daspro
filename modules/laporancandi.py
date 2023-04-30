def laporancandi(candi: list, panjang_candi: int)-> None:
    totalcandi = panjang_candi-1
    if panjang_candi>=101:
        totalcandi = 100
    
    pasir = 0
    batu = 0
    air = 0
    for i in range (1,101):
        if candi[i][0] != "none":
            pasir += int(candi[i][2])
            batu += int(candi[i][3])
            air += int(candi[i][4])
        

    harga_termahal = 0
    for i in range(1,101):
        if candi[i][0] != "none":
            harga = (10000*(int(candi[i][2]))+(15000*(int(candi[i][3])))+(7500*(int(candi[i][4]))))
            if harga>=harga_termahal:
                harga_termahal = harga
                index1 = i
    
    if totalcandi != 0:
        candi_termahal = candi[index1][0] 
            
    if candi[1][0] != "none":
        harga_termurah = (10000*(int(candi[1][2]))+(15000*(int(candi[1][3])))+(7500*(int(candi[1][4]))))
        index2 = 1
        for i in range(1,101):
            if candi[i][0] != "none":
                harga = (10000*(int(candi[i][2]))+(15000*(int(candi[i][3])))+(7500*(int(candi[i][4]))))
                if harga<=harga_termurah:
                    harga_termurah = harga
                    index2 = i

    if totalcandi != 0:
        candi_termurah = candi[index2][0] 

    print(f"\n> Total Candi: {totalcandi}")
    print(f"> Total Pasir yang digunakan: {pasir}")
    print(f"> Total Batu yang digunakan: {batu}")
    print(f"> Total Air yang digunakan: {air}")
    if totalcandi == 0:
        print("> ID Candi Termahal: -")
        print("> ID Candi Termurah: -")
    else:
        print(f"> ID Candi Termahal: {candi_termahal} (Rp {harga_termahal})")
        print(f"> ID Candi Termurah: {candi_termurah} (Rp {harga_termurah})")

