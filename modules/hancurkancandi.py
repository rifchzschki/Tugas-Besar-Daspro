def cek_candi(candi, hancurkan):
    i = 0
    found = False
    while i < 101 and not found:
        if candi[i][0] == str(hancurkan):
            found = True
        i+=1
    return found        
        
def hancurkancandi(candi):
    hancurkan = int(input('Masukkan ID candi: '))
    if hancurkan > 100:
        print("Tidak ada candi dengan id tersebut.") 
    else:
        YorN = False
        while not YorN:
            yakin = input(f'Apakah Anda yakin ingin menghancurkan candi ID: {hancurkan} (Y/N)? ')
            if yakin == 'Y' or yakin=='y':
                YorN = True
                if cek_candi(candi, hancurkan) :#cek apakah ada candi dengan id tersebut 
                    print(f'Candi ID: {hancurkan} berhasil dihancurkan')
                    candi[hancurkan] = ["none", "none", "none", "none", "none"]
                else:
                    print(f'Candi ID: {hancurkan} tidak ditemukan')
                
            elif yakin=='N' or yakin=='n':
                print(f'Candi ID: {hancurkan} tidak jadi dihancurkan')
                YorN = True
            else:
                continue
