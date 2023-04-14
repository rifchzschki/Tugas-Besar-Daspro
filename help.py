def help(role):
    # pemain belum login
    if  role == "none" :
        print ("==================== HELP ====================")
        print ("1. login \nUntuk masuk menggunakan akun \n2. exit \nUntuk keluar dari program dan kembali ke terminal")
    else :
        if role == "Bandung Bondowoso":
            print ("==================== HELP ====================")
            print ("1. logout \nUntuk keluar dari akun yang digunakan sekarang \n2. summonjin \nUntuk memanggil jin")
            print ("3. hapus jin \nUntuk menghapus jin \n4. ubah jin \nUntuk mengubah tipe jin")
            print ("5. kumpul/bangun \nUntuk mengarahkan seluruh pasukan jin untuk mengumpulkan bahan atau membangun candi \n6. laporan jin \nUntuk mengetahui kinerja dari para jin")
            print ("7. laporan candi \nUntuk mengetahui progress pembagunan candi")
        elif role == "Roro Jonggrang":
            print ("==================== HELP ====================")
            print ("1. logout \nUntuk keluar dari akun yang digunakan sekarang \n2. hancurkancandi \nUntuk menghancurkan candi yang tersedia")
            print ("3. ayamberkokok \nUntuk menyelesaikan permainan dengan memalsukan pagi har")
        elif role == "Jin Pengumpul":
            print ("==================== HELP ====================")
            print ("1. logout \nUntuk keluar dari akun yang digunakan sekarang \n2. kumpul \nUntuk mengumpulkan resource candi")
        elif role == "Jin Pembangun":
            print ("==================== HELP ====================")
            print ("1. logout \nUntuk keluar dari akun yang digunakan sekarang \n2. bangun \nUntuk membangun candi")
        else :
            print ("Tidak valid")