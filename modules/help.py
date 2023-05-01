# F15: Help

def help(role: str)-> None:
# Menjelaskan fitur apa saja yang dimiliki oleh setiap role

# Kamus Lokal

# Algoritma
    if  role == "none" :
        print ("==================== HELP ====================")
        print ("1. login \nUntuk masuk menggunakan akun \n2. exit \nUntuk keluar dari program dan kembali ke terminal.")
    else :
        if role == "bandung_bondowoso":
            print ("==================== HELP ====================")
            print ("1. logout \nUntuk keluar dari akun yang digunakan sekarang. \n2. summonjin \nUntuk memanggil jin.")
            print ("3. hapusjin \nUntuk menghapus jin. \n4. ubahjin \nUntuk mengubah tipe jin.")
            print ("5. batchkumpul \nUntuk mengarahkan seluruh pasukan jin untuk mengumpulkan bahan. \n6. batchbangun \nUntuk mengarahkan seluruh pasukan jin untuk membangun candi. \n7. laporanjin \nUntuk mengetahui kinerja dari para jin.")
            print ("8. laporancandi \nUntuk mengetahui progress pembagunan candi.")
            print ("9. save \nUntuk menyimpan data perubahan.")
        elif role == "roro_jonggrang":
            print ("==================== HELP ====================")
            print ("1. logout \nUntuk keluar dari akun yang digunakan sekarang. \n2. hancurkancandi \nUntuk menghancurkan candi yang tersedia.")
            print ("3. ayamberkokok \nUntuk menyelesaikan permainan dengan memalsukan pagi hari.")
            print ("4. save \nUntuk menyimpan data perubahan.")        
        elif role == "jin_pengumpul":
            print ("==================== HELP ====================")
            print ("1. logout \nUntuk keluar dari akun yang digunakan sekarang. \n2. kumpul \nUntuk mengumpulkan resource candi.")
            print ("3. save \nUntuk menyimpan data perubahan.")
        elif role == "jin_pembangun":
            print ("==================== HELP ====================")
            print ("1. logout \nUntuk keluar dari akun yang digunakan sekarang. \n2. bangun \nUntuk membangun candi.")
            print ("3. save \nUntuk menyimpan data perubahan.")
        else :
            print ("Tidak valid")