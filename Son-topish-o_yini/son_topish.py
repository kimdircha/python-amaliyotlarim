""" Son topish o'yini
    Muallif: Suhayl Qodirov
    17.03.2021"""

import random as rdm
# < soz topish from button / Games.game statedan -> Games.findBotsNumber
# ? config.FINDNUMBER[message.from_user.id] = {}

# >\"Son topish\" o'yinini o'ynaymiz.
# >\nMen 0 va 100 oralig'idan bir son o'yladim. Uni topishga urinib ko'ring:
# ? config.FINDNUMBER[message.from_user.id]['playersAttemps'] = 0
# ? config.FINDNUMBER[message.from_user.id]['computersChoise'] = rdm.randint(0,100)
# ? computersAttemps=0
# ? lowerLimit=0
# ? upperLimit=100
# ? computersGuess=rdm.randint(lowerLimit,upperLimit)

# < number

# ? try config.FINDNUMBER[message.from_user.id]['playersGuess'] = int msg.text
# ? except > qoida buzildi, yutdim / -> Games.game
# ? else 
# ? config.FINDNUMBER[message.from_user.id]['playersAttemps'] += 1
# ? if computersChoise==playersGuess:
#     > f"To'g'ri, men o'ylagan son {computersChoise} edi."
#     ? -> Games.findPlayerssNumber
#     > f"Qoyil {playersAttemps} ta urinishda topdingiz. "
#                f"Endi siz son o'ylang va 'Enter'ni bosing. Men uni topishga urinib ko'raman."
# ? elif computersChoise<playersGuess:
#     > f"O'ylagan sonim {playersGuess}dan kichik.\n>>> "
# ? else:
#     f"O'ylagan sonim {playersGuess}dan katta.\n>>> "

# < boshlash from buttton /state = Games.findPlayerssNumber

# ? computersAttemps+=1
# > f"Siz o'ylagan son {computersGuess}mi?\n"
#         	          f"\nAgar siz o'ylagan son {computersGuess}dan katta bo'lsa + deb, kichik bo'lsa - deb, to'g'ri topgan bo'lsam ha deb yozing >>> "
#     with inline buttons

# if call.data=='+':
#     lowerLimit=computersGuess+1
#     if lowerLimit>upperLimit:
#         > "\nYolg'on gapirdingiz! O'yin qoidasi buzildi."
#         computersAttemps=0
#         -> Games.game
#     computersGuess=rdm.randint(lowerLimit,upperLimit)
# elif call.data=='-':
#     upperLimit=computersGuess-1
#     if lowerLimit>upperLimit:
#         > "\nYolg'on gapirdingiz! O'yin qoidasi buzildi."
#         computersAttemps=0
#         -> Games.game
#     computersGuess=rdm.randint(lowerLimit,upperLimit)
# else:
#     > f"Men {computersAttemps} ta urinishda topdim"
#     -> Games.game

# if playersAttemps>computersAttemps:
#     > "Men g'olibman!"
# elif playersAttemps<computersAttemps:
#     > "Siz g'olibsiz!"
# else:
#     > "Durrang!"

# > "O'yin tugadi!"

print("\nAssalomu aleykum. Keling, \"Son topish\" o'yinini o'ynaymiz.")
while True:
    playersGuess=int(input("\nMen 0 va 100 oralig'idan bir son o'yladim. Uni topishga urinib ko'ring:\n>>> "))
    playersAttemps=0
    computersChoise=rdm.randint(0,100)
    while True:
        playersAttemps+=1
        if computersChoise==playersGuess:
            print(f"To'g'ri, men o'ylagan son {computersChoise} edi.")
            break
        elif computersChoise<playersGuess:
            playersGuess=int(input(f"O'ylagan sonim {playersGuess}dan kichik.\n>>> "))
        else:
            playersGuess=int(input(f"O'ylagan sonim {playersGuess}dan katta.\n>>> "))
    input(f"Qoyil {playersAttemps} ta urinishda topdingiz. "
               f"Endi siz son o'ylang va 'Enter'ni bosing. Men uni topishga urinib ko'raman.")
    computersAttemps=0
    lowerLimit=0
    upperLimit=100
    computersGuess=rdm.randint(lowerLimit,upperLimit)
    while True:
        computersAttemps+=1
        isEqual=input(f"Siz o'ylagan son {computersGuess}mi?\n"
        	          f"\nAgar siz o'ylagan son {computersGuess}dan katta bo'lsa + deb, kichik bo'lsa - deb, to'g'ri topgan bo'lsam ha deb yozing >>> ")
        if isEqual=='+':
            lowerLimit=computersGuess+1
            if lowerLimit>upperLimit:
                print("\nYolg'on gapirdingiz! O'yin qoidasi buzildi.")
                computersAttemps=0
                break
            computersGuess=rdm.randint(lowerLimit,upperLimit)
        elif isEqual=='-':
            upperLimit=computersGuess-1
            if lowerLimit>upperLimit:
                print("\nYolg'on gapirdingiz! O'yin qoidasi buzildi.")
                computersAttemps=0
                break
            computersGuess=rdm.randint(lowerLimit,upperLimit)
        else:
            print(f"Men {computersAttemps} ta urinishda topdim")
            break
    if playersAttemps>computersAttemps:
        print("Men g'olibman!")
    elif playersAttemps<computersAttemps:
        print("Siz g'olibsiz!")
    else:
        print("Durrang!")
    playAgain=input("Yana o'ynaysizmi? (ha/yo'q)\n>>> ")
    if playAgain!="ha":
        break
print("O'yin tugadi!")
