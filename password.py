from string import *
from itertools import product

value =  ascii_letters + digits + punctuation
for i in range(1,4):
    for j in product(value, repeat=i):
        word = "".join(j)
        p = open("passwords.txt","a")
        p.write(word)
        p.write("\n")