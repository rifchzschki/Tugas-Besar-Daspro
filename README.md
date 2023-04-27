# Tugas-Besar-Daspro
## Program sederhana dalam membuat permainan dalam python
<br>

> *Kalo mau ubah fungsi yang udah ada diskusiin dulu di grup yaa...* <br>
> *Sebelum ngelakuin perubahan, pull terlebih dahulu perubahan yang udah ada biar liat skema programnya gimana.*

<br>

### Struktur data program
---
```
folder_game
--> save_1
--> save_2
--> ....
modules
--> helper.py
--> login.py
--> hapusjin.py
--> save.py
--> ...
main.py
README.md

```
---
<br>

### Hal yang perlu direvisi <br>
*  (15/4/2023)<br>
    * exit --> output jika masukan selain y/n<br> 
    * kumpul --> jangan cuma print tapi harus bisa nyimpen di array program utama<br>
    * logout --> (coba nnti liat main.py yang baru trs liat codenya), gw ada ide gmn klo logout ini dalam bentuk fungsi trs return nya berupa boolean pengganti logout di main.py<br>
    * login --> kondisi ketika False masih unsolved 
        1. ~~ketika pertama kali login, pass salah. lalu memasukan password benar, munculnya username tidak terdaftar.~~ (solved => membenarkan logika if else nya)
        2. ~~ketika setelah login user pertama, lalu logout kemudian login lagi dengan user baru, error~~ (solved => mengganti nama fungsi role agar tidak menyebabkan error)
    * Arraynya harus statis cenah
    
---

* (18/042023)<br>
    * Array sudah statis dengan value kosong diberi tanda "none"
    * fungsi yang sudah selesai => (summonjin, hapusjin, ubahjin, login, logout, load, ayamberkokok, help, randomnumber, jinpengumpul, jinpembangun, hancurkancandi, exit)
    * fungsi yang belum => (save, laporancandi, laporanjin, batchkumpul/bangun)
    * helper blm dirapihin

* (21/04/2023) <br>
    * fungsi yang sudah ditambahkan => (batchkumpul/bangun, save)
    * fungsi yang belum => (laporancandi, laporanjin)
    * helper blm dirapihin

* (24/04/2023) <br>
    * masalah yang ditemukan : 
        1. ~~batchbangun belum bisa menaruh data pembuat candi (jumlah sisa, data pembuat, id, bahan percandi)~~
        2. ~~keanehan terjadi pada fungsi kumpul, jadi gabisa print~~
        3. ~~pada fungsi save, tidak bisa menambahkan integer pada string pada convert_arr_str~~

* (26/04/2023) <br>
        1. ~~hapusjin hanya bisa hapus jin sekali~~
        2. ~~jumlah candi batchbangun dengan bangun masih belum relevan~~