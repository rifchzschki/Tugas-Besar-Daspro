def hancurkancandi():
    hancurkan = int(input('Masukkan ID candi: '))
    YorN = False

    while YorN == False:
        yakin = input(f'Apakah Anda yakin ingin menghancurkan candi ID: {hancurkan} (Y/N)? ')
        if yakin == 'Y' or yakin=='y':
            YorN = True
            if  :
            else:
                print(f'Candi ID: {hancurkan} tidak ditemukan')
            print(f'Candi ID: {hancurkan} berhasil dihancurkan')
        elif yakin=='N' or yakin=='n':
            print(f'Candi ID: {hancurkan} tidak jadi dihancurkan')
            YorN = True
        else:
            continue
