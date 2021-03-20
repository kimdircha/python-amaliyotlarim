""" So'z topish o'yini
    Muallif: Suhayl Qodirov
    18.03.2021 """

from uzwords import words
import random as rdm

def harf_tekshir(harf, harflar, ishlatilgan, yechim):
    if harf in harflar:
        print("\nTo'g'ri\n\nSiz ishlatgan harflar: ", end='')
        for ishlatilgan_harf in ishlatilgan:
            print(ishlatilgan_harf, end='')
        print()
        for kv in yechim:
            print(kv, end=' ')
    else:
        print("\nNoto'g'ri\n\nSiz ishlatgan harflar: ", end='')
        for ishlatilgan_harf in ishlatilgan:
            print(ishlatilgan_harf, end='')
        print()
        for kv in yechim:
            print(kv, end=' ')  
        
def kv_och(yechim):
    for tek in range(len(harflar)):
        if harflar[tek] == harf:
            yechim[tek] = harf.upper()
    return yechim

jumboq=rdm.choice(words)
while '-' in jumboq or ' ' in jumboq:
    jumboq=rdm.choice(words)

harflar = []
for harf in jumboq:
    harflar.append(harf)
    
print(f"Men {len(harflar)} ta harfdan iborat bir so'z o'yladim.")

yechim = []
ishlatilgan = []

for uzunlik in harflar:
    yechim.append('□')
    
for kv in yechim:
    print(kv, end=' ')

while '□' in yechim:
    harf = input("\nTaxmin qiling: ")
    if harf.upper() in ishlatilgan:
        print(f"\n{harf.upper()} harfi ishlatilgan.", end='')
    else:
        ishlatilgan.append(harf.upper())
        yechim = kv_och(yechim[:])
        harf_tekshir(harf, harflar[:], ishlatilgan[:], yechim[:])

print(f"\n\n"
      f"Siz {len(ishlatilgan)} ta urinishda so'zni topdingiz.")
input()