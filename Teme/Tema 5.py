# 1.
def suma_2_numere(a, b):
    rezultat = a + b
    return rezultat

print(suma_2_numere(2, 26))
print('-----------------------------')

# 2.
def nr_par_test(a):
    if a % 2 == 0:
        par=True
    else:
        par=False
    return par

print(nr_par_test(2))
print('-----------------------------')

# 3.
def caractere(nume, prenume, nume_mijlociu):
    a = len(nume) + len(prenume) + len(nume_mijlociu)
    return a

print(caractere('Sopterean', 'Cezar', ''))
print('-----------------------------')

# 4.
def aria_drept(L, l):
    aria = L * l
    return aria

print(aria_drept(5, 8))
print('-----------------------------')

# 5
def aria_cerc(R):
    Pi=3.14
    aria = Pi * R**2
    return aria

print(aria_cerc(6))
print('-----------------------------')

# 6.
def caracterX(text):
    adv_sau_fals=False
    if text.find('X') > 0:
        adv_sau_fals=True
        return  adv_sau_fals
    else:
        return  adv_sau_fals

print(caracterX('Emisiunea urmatoare este X-Factor'))
print('-----------------------------')

# 7.
def counter(Text):
    lower=0
    upper=0
    for l in Text:
        if l.isalpha() and l.islower():
            lower+=1
    for u in Text:
        if u.isalpha() and u.isupper():
            upper+=1
    print(f'Nr de caractere lower case este {lower}')
    print(f'Nr de caractere upper case este {upper}')

counter('String random pentru EX: 7')
print('-----------------------------')

# 8.
def lista_poz():
    lista=list(input('Introduceri lista de nr: ').split())
    poz=[]
    for a in lista:
        if int(a) > 0:
            poz.append(int(a))
    return poz

# print(lista_poz())
print('-----------------------------')

# 9.
def mic_mare(x, y):
    if x > y:
        print(f'Primul numar {x} este mai mare decat al doilea numar {y}')
    elif x < y:
        print(f'Al doilea numar {y} este mai mare decat primul numar {x}')
    else:
        print('Numerele sunt egale')

mic_mare(4, 7)
print('-----------------------------')

# 10.
def adaugare_in_set():
    adaugat=False
    print('Adaugati nr: ')
    a=input()
    print('Adaugati setul de nr: ')
    b=list(input().split())
    if b.count(a) == 0:
        b.append(a)
        adaugat=True
        print('Am adaugat numărul nou în set')
        return adaugat
    else:
        print('Nu am adaugat numărul în set. Acesta există deja')
        return adaugat

print(adaugare_in_set())
