def cek_candi(candi, hancurkan):
    i = 0
    found = False
    while i < 101 and not found:
        if candi[i][0] == str(hancurkan):
            found = True
        i+=1
    return found        

def hapuscandi(candi, idx):
    for i in range (1,101):
        if candi[i][0] == idx:
            candi[i] = ["none", "none", "none", "none", "none"]
        

def hancurkancandi(candi):
    hancurkan = int(input('Masukkan ID candi: '))
    if hancurkan > 100:
        print("Tidak ada candi dengan ID tersebut.") 
    else:
        YorN = False
        if cek_candi(candi, hancurkan):
            while not YorN:
                yakin = input(f'Apakah Anda yakin ingin menghancurkan candi ID: {hancurkan} (Y/N)? ')
                if yakin == 'Y' or yakin=='y':
                    YorN = True
                    for i in range (1,101):
                        if candi[i][0] != "none":
                            if int(candi[i][0]) == hancurkan:
                                candi[i] = ["none", "none", "none", "none", "none"]
                    print(f'Candi ID: {hancurkan} berhasil dihancurkan')
                elif yakin=='N' or yakin=='n':
                    print(f'Candi ID: {hancurkan} tidak jadi dihancurkan')
                    YorN = True
                else:
                    continue
        else:
            print(f'Tidak ada candi ID: {hancurkan}')
