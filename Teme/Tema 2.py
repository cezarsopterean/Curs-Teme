#1.
# if else este un mod de a controla flow-ul codului, executand o anumita linie de cod in functie de conditiile date

x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))
print('-------------------------------------')
#2.
if x > 0:
    print('x este numar natural')
else:
    print('x nu este numar natural')
print('-------------------------------------')

#3.
if x > 0:
    print('x este numar pozitiv')
elif x < 0:
    print('x este numar negativ')
else:
    print('x este numar neutru')
print('-------------------------------------')

#4.
if x > -2 and x < 13:
    print('x se aflta intre -2 si 13')
else:
    print('x nu se afla intre -2 si 13')
print('-------------------------------------')

#5.
if x - y < 5 and x - y >= 0:
    print('diferenta este mai mica de 5')
else:
    print('diferenta este mai mare de 5')
print('-------------------------------------')

#6.
if not(x > 5 and x < 27):
    print('x nu este intre 5 si 27')
else:
    print('x este intre 5 si 27')
print('-------------------------------------')

#7.
if x == y:
    print('x este egal cu y')
elif x > y:
    print ('x este mai mare')
elif y > x:
    print('y este mai mare')
print('-------------------------------------')

#8.
if x == y == z:
    print('Triunghi echilateral')
elif x == y or x == z or y == z:
    print('Triunghi isoscel')
else:
    print('Triunghi oarecare')
print('-------------------------------------')

#9.
vocale = ('a', 'e', 'i', 'o', 'u')
litera = input('Scrie litera: ')
if litera in vocale:
    print(f'{litera} este o vocala')
else:
    print(f'{litera} nu este o vocala')
print('-------------------------------------')

#10.
nota = float(input('Introduceti nota: '))
if nota >= 9 and nota <= 10:
    nota = 'A'
elif nota >= 8 and nota < 9:
    nota = 'B'
elif nota >= 7 and nota < 8:
    nota = 'C'
elif nota >= 6 and nota < 7:
    nota = 'D'
elif nota >= 4 and nota < 6:
    nota = 'E'
elif nota >= 0 and nota < 4:
    nota = 'F'
else:
    print('Nota invalida, doar de la 0 la 10')
print(f'Nota este {nota}')


list = ('cezar', 'alex')
print(list.index('alex'))