# 1.

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']

# For
print('---------------------------')
for a in range(len(masini)):
    print(f'Masina mea preferata este {masini[a]}')

# For each
print('---------------------------')
for masina in masini:
    print(f'Masina mea preferata este {masina}')

# While
print('---------------------------')
m=0
while m < len(masini):
    print(f'Masina mea preferata este {masini[m]}')
    m+=1

# 2.
print('---------------------------')
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']

for i in range(1, len(masini)-1):
    masini[i]=masini[i].upper()
else:
    print(masini)

# 3.
print('---------------------------')
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']

b=0
while b <len(masini):
    if masini[b] == 'Mercedes':
        print('Am gasit masina dorita de dvs.')
        break
    else:
        print(f'Am gasit masina {masini[b]}, mai cautam')
        b+=1

# 4.
print('---------------------------')
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']

for j in masini:
    if j == 'Trabant' or j == 'Lăstun':
        continue
    print(f'S-ar putea sa va placa masina {j}')

# 5.
print('---------------------------')
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']
masini_vechi=[]

for modele_vechi in range(0, len(masini)):
    if masini[modele_vechi] == 'Trabant' or masini[modele_vechi] == 'Lăstun':
        masini_vechi.append(masini[modele_vechi])
        masini[modele_vechi]='Tesla'
print(f'Modele vechi: {masini_vechi}')
print(f'Modele noi: {masini}')

# 6.
print('---------------------------')
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
lista_masini=[]
for p in pret_masini:
    if pret_masini.get(p) < 15000:
        lista_masini.append(p)
print(f'Pentru un buget de sub 15000 euro puteti alege masina {lista_masini}')

# 7.
print('---------------------------')
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
nr3=0
for n in numere:
    if n == 3:
        nr3+=1
print(f'Nr 3 apare de {nr3} ori')

# 8.
print('---------------------------')
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma=0
for n in numere:
    suma+=n
print(f'Suma nr este {suma}')

# 9.
print('---------------------------')
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

nr_max=0
for nr in numere:
    if nr > nr_max:
        nr_max=nr
print(f'Cel mai mare nr este {nr_max}')

# 10.
print('---------------------------')
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for nrpoz in range(0, len(numere)):
    if numere[nrpoz] > 0:
        numere[nrpoz] = -numere[nrpoz]
print(f'Lista noua este {numere}')