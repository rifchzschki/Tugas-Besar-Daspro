def ayamberkokok(panjang: int)-> None:
    print('Kukuruyuk... Kukuruyuk...\n')
    jumlah_candi= (panjang-1)
    if jumlah_candi > 100:
        jumlah_candi = 100
    print(f"Jumlah Candi: {jumlah_candi}\n")
    if jumlah_candi <100:
        print('Selamat, Roro Jonggrang memenangkan permainan!')
        print('\n*Bandung Bondowoso marah*')
        print('Roro Jonggrang dikutuk menjadi candi')
    else :
        print('Yah, Bandung Bondowoso memenangkan permainan!')
    exit()