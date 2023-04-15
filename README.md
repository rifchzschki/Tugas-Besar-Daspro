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
        1. ketika pertama kali login, pass salah. lalu memasukan password benar, munculnya username tidak terdaftar.
        2. ketika setelah login user pertama, lalu logout kemudian login lagi dengan user baru, error
    
---