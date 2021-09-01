""" So'z topish o'yini
    Muallif: Suhayl Qodirov
    18.03.2021 """

from uzwords import words
import random as rdm

def check_letter(letter, letters, used, solution):
    if letter in letters:
        print("\nTo'g'ri\n\nSiz ishlatgan harflar: ", end='')
    else:
        print("\nNoto'g'ri\n\nSiz ishlatgan harflar: ", end='')
    for used_letter in used:
        print(used_letter, end='')
    print()
    for item in solution:
        print(item, end=' ')  
        
def open_found(solution, letter, letters):
    for index in range(len(letters)):
        if letters[index] == letter:
            solution[index] = letter.upper()
    return solution

puzzle=rdm.choice(words)

letters = []
solution = []
used = []
for letter in puzzle:
    letters.append(letter)
    solution.append('□')
    
print(f"Men {len(letters)} ta harfdan iborat bir so'z o'yladim.")

for item in solution:
    print(item, end=' ')

while '□' in solution:
    letter = input("\nTaxmin qiling: ")
    if letter.upper() in used:
        print(f"\n{letter.upper()} harfi ishlatilgan.", end='')
    else:
        used.append(letter.upper())
        solution = open_found(solution[:], letter, letters[:])
        check_letter(letter, letters[:], used[:], solution[:])

print(f"\n\n"
      f"Siz {len(used)} ta urinishda so'zni topdingiz.")
input()
