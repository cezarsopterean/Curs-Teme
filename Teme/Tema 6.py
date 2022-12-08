# 1.

class Cerc():
    raza=None
    culoare=None

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f'Raza cercului este {self.raza}')
        print(f'Culoarea cercului este {self.culoare}')

    def aria(self):
        aria_cerc = 3.14 * self.raza**2
        print(f'Aria cercului este {aria_cerc}')

    def diametru(self):
        diametrul = 2 * self.raza
        print(f'Diametrul cercului este {diametrul}')

    def circumferinta(self):
        circ = 3.14 * (self.raza * 2)
        print(f'Circumferinta cercului este {circ}')

cerc = Cerc(5, 'albastru')
cerc.aria()
cerc.descrie_cerc()
cerc.diametru()
cerc.circumferinta()
print('-------------------------------------')
# 2.

class Dreptunghi():
    lungime=None
    latime=None
    culoare=None

    def __init__(self, lungime, latime, culoare):
        self.lungime= lungime
        self.latime= latime
        self.culoare = culoare

    def descrie(self):
        print(f'Lungimea dreptunghiului este {self.lungime}')
        print(f'Latimea dreptunghiului este {self.latime}')
        print(f'Culoarea dreptunghiului este {self.culoare}')

    def aria(self):
        a = self.lungime * self.latime
        print(f'Aria dreptunghi = {a}')

    def perimetrul(self):
        p = 2 * (self.lungime+self.latime)
        print(f'Perimetru dreptunghi = {p}')

    def schimba_culoarea(self, culoare_noua):
        self.culoare = culoare_noua

drept = Dreptunghi(9, 10, 'alb')
drept.descrie()
drept.aria()
drept.perimetrul()
drept.schimba_culoarea('Verde')
drept.descrie()
print('-------------------------------------')

# 3.

class Angajat():
    nume=None
    prenume=None
    salariu=None

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f'Angajatul cu numele {self.nume} si prenumele {self.prenume} are salariu de {self.salariu} de lei')

    def nume_complet(self):
        print(f'Numele complet : {self.nume} {self.prenume}')

    def salariu_lunar(self):
        print(f'Salariu lunar de {self.salariu}')

    def salariu_anual(self):
        sal_an = self.salariu * 12
        print(f'Salariu anual de {sal_an}')

    def marire_salariu(self, procent):
        marire = (self.salariu/100) * procent
        self.salariu = self.salariu + marire
        print(f'Salariu a fost marit cu {procent}% la {self.salariu}')

ang = Angajat('Alex', 'Popica', 4000)
ang.descrie()
ang.nume_complet()
ang.salariu_lunar()
ang.salariu_anual()
ang.marire_salariu(5)
ang.salariu_lunar()
ang.salariu_anual()
print('-------------------------------------')

# 4.
class Cont():
    iban = None
    titular_cont = None
    sold = None

    def __init__(self, iban, titular, sold):
        self.iban = iban
        self.titular_cont = titular
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul "{self.titular_cont}" are in contul: "{self.iban}" | suma de {self.sold} lei.')

    def debitare_cont(self, sumad):
        self.sold = self.sold + sumad

    def creditare_cont(self, sumac):
        self.sold = self.sold + sumac

cont = Cont('RO12BTCD231b165s63ydc6', 'Alexandru Posh Gabriel', 20000)
cont.afisare_sold()
cont.debitare_cont(10000)
cont.afisare_sold()
cont.creditare_cont(5000)
cont.afisare_sold()
print('-------------------------------------')