# 1.
x = int(input('x = '))
if len(str(x)) >= 4:
    print(f'x are {len(str(x))} cifre')
else:
    print('x are mai putin de 4 cifre')
print('----------------------------------------')

# 2.
x = int(input('x = '))
x_de_6 = False
if len(str(x)) == 6:
    x_de_6 = True
print(f'x are 6 cifre = {x_de_6}')
print('----------------------------------------')

# 3.
x = int(input('x = '))
if x % 2 == 0:
    nr='par'
else:
    nr='impar'
print(f'x este numar {nr}')
print('----------------------------------------')

# 4.
x=int(input('x = '))
y=int(input('y = '))
z=int(input('z = '))
if x > y and x > z:
    nr_mare='x'
    val=x
elif y > x and y > z:
    nr_mare='y'
    val=y
else:
    nr_mare='z'
    val=z
print(f'Nr cel mai mare este: {nr_mare} cu valoare de {val}')
print('----------------------------------------')

# 5.
x=20
y=10
z=300
if (x>0) and (y>0) and (z>0) and ((x+y>z) or (x+z>y) or (y+z>x)):
    valid=True
else:
    valid=False
print(f'Triughiul este valid: {valid}')
print('----------------------------------------')

# 6.
Text='Coral is either the stupidest animal or the smartest rock'
x = int(input('Introduceti numar: '))
print(Text[:-x:])
print('----------------------------------------')

# 7.
Text_nou=Text[:5:]+Text[-5::]
print(Text_nou)
print('----------------------------------------')

# 8.
Text ='Coral is either the stupidest animal or the smartest rock'
x = Text.find('rock')
print(Text[:x:])
print('----------------------------------------')

# 9.
String=input('Introduceti text: ').lower()
assert String[:1:] == String[:-2:-1], 'Prima litera nu este la fel ca si ultima'; print('Prima si ultima litera sunt la fel')
print('----------------------------------------')

# 10.
numere='0123456789'
nr_pare=numere[::2]
nr_impare=numere[1::2]
print(f'Nr pare: {nr_pare}')
print(f'Nr impare: {nr_impare}')
print('----------------------------------------')

# Extra
from random import randrange
dice_roll = randrange(1,6)
guess = int(input('Introduceti numar de la 1 la 6: '))
win = False
if guess > dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {guess} dar a fost {dice_roll}')
elif guess < dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {guess} dar a fost {dice_roll}')
else:
    win = True
    print(f'Ai ghicit. Felicitari! Ai ales {guess} si zarul a fost {dice_roll}')
if win == True:
    print('+100$')