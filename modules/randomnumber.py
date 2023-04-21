import time

def lcg(x):
    seed = int(time.time() * (10**7)) 
    a = [75, 1664525, 22695477]
    c = [74, 1013904223, 1]
    m = [2**16 + 1, 2**32, 2**32]
    unit = 3
    num_base = seed + (x*18)%5
    arr = [0 for i in range(unit)]
    for i in range(unit):
        rd = (a[i] * num_base + c[i]) % m[i]
        arr[i] = (rd%6)
        num_base = rd + i
    return (arr)
