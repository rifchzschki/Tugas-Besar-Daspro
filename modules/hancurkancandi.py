def hancurkancandi():
    hancurkan = int(input('Masukkan ID candi: '))
    YorN = False

    while YorN == False:
        yakin = input(f'Apakah Anda yakin ingin menghancurkan candi ID: {hancurkan} (Y/N)? ')
        if yakin == 'Y' or yakin=='y':
            YorN = True
            if  : 
                print(f'Candi ID: {hancurkan} berhasil dihancurkan')
            else:
                print(f'Candi ID: {hancurkan} tidak ditemukan')
            
        elif yakin=='N' or yakin=='n':
            print(f'Candi ID: {hancurkan} tidak jadi dihancurkan')
            YorN = True
        else:
            continue
