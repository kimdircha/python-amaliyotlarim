""" Son topish o'yini
    Muallif: Suhayl Qodirov
    17.03.2021"""

import random as rdm
print(f"\nAssalomu aleykum. Keling, \"Son topish\" o'yinini o'ynaymiz.")
while True:
    b=int(input("\nMen 0 va 10 oralig'idan bir son o'yladim. Uni topishga urinib ko'ring:\n>>> "))
    n=0
    a=rdm.randint(0,10)
    while True:
        n+=1
        if a==b:
            print(f"To'g'ri, men o'ylagan son {a} edi.")
            break
        elif a<b:
            b=int(input(f"O'ylagan sonim {b}dan kichik.\n>>> "))
        else:
            b=int(input(f"O'ylagan sonim {b}dan katta.\n>>> "))
    input(f"Qoyil {n} ta urinishda topdingiz. "
               f"Endi siz son o'ylang va 'Enter'ni bosing. Men uni topishga urinib ko'raman.")
    m=0
    p=0
    q=10
    y=rdm.randint(p,q)
    while True:
        m+=1
        tek=input(f"Siz o'ylagan son {y}mi?\n"
        	          f"\nAgar siz o'ylagan son {y}dan katta bo'lsa + deb, kichik bo'lsa - deb, to'g'ri topgan bo'lsam ha deb yozing >>> ")
        if tek=='+':
            p=y+1
            if p>q:
                print("\nYolg'on gapirdingiz! O'yin qoidasi buzildi.")
                m=0
                break
            y=rdm.randint(p,q)
        elif tek=='-':
            q=y-1
            if p>q:
                print("\nYolg'on gapirdingiz! O'yin qoidasi buzildi.")
                m=0
                break
            y=rdm.randint(p,q)
        else:
            print(f"Men {m} ta urinishda topdim")
            break
    if n>m:
        print("Men g'olibman!")
    elif n<m:
        print("Siz g'olibsiz!")
    else:
        print("Durrang!")
    oo=input("Yana o'ynaysizmi? (ha/yo'q)\n>>> ")
    if oo!="ha":
        break
print("O'yin tugadi!")