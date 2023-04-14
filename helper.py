def panjang(array) -> int: 
# Menghitung Panjang List
# count : int
    count = 0
    for i in array:
        count +=1
    return count

# lcg belum jadi wait 
# LCG formula --> X(k+1) = ((a * Xk) + c) % m
# seed = int(input("Seed number: "))
# a = int(input("Multiplier (a): "))
# c = int(input("Increment (c): "))
# m = int(input("Modulus (m): "))
# unit = int(input("How many random numbers would you like to generate?\nInput: "))

# def lcg():
#     num_base = seed
#     for i in range(unit, 0, -1):
#         rd = (a * num_base + c) % m
#         print(rd)
#         num_base = rd