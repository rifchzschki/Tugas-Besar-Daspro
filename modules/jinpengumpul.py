from modules.randomnumber import *

def kumpul(bahan):
   
    p = lcg(1)    
    print (f"Jin menemukan {p[0]} pasir, {p[1]} batu, dan {p[2]} air.")
    if bahan[1][2] == "none":
        bahan[1] =["pasir", "desc", p[0]]
        bahan[2] =["batu", "desc", p[1]]
        bahan[3] =["air", "desc", p[2]]
    else:
        pasir = bahan[1][2] + p[0]
        batu = bahan[2][2] + p[1]
        air = bahan[3][2] + p[2]
        bahan[1] =["pasir", "desc", pasir]
        bahan[2] =["batu", "desc", batu]
        bahan[3] =["air", "desc", air]

