#1. Variabila = o zona din memorie in care se stocheaza date

#2.
produs = 'sapun'
produse_vandute = 536
pret_bucata = 2.99
in_stock = True

#3.
print(type(produs))
print(type(produse_vandute))
print(type(pret_bucata))
print(type(in_stock))

#4.
pret_bucata = float(round(pret_bucata))
print(pret_bucata)

#5.
print('Ati ales produsul : ' + produs)
print('Numarul de vanzari pana in acest moment : ' + str(produse_vandute))
print('Pretul total va fi : ' + str(pret_bucata * 5))
print('Produs in stock : ' + str(in_stock))

6.
Nume = input('Introduceti numele: ')
Prenume = input('Introduceti prenumele: ')
print(len(Nume + Prenume))

7.
lungimea = input('Introduceti lungimea: ')
latimea = input('Introduceti latimea: ')
print('Aria dreptunghiunlui este: ' + str(int(lungimea) * int(latimea)))

#8.
propozitia1 = 'Coral is either the stupidest animal or the smartest rock'
print('Cuvantul "the" apare de ' + str(propozitia1.count('the ')) + ' ori')

#9
propozitia2 = propozitia1.replace('the ', 'THE ')
print('Cuvantul "the" apare de ' + str(propozitia2.count('THE ')) + ' ori')

#10
assert propozitia1.isnumeric() == True, "Nu contine doar numere"
print('Contine doar numere')
