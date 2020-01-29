#Proiect final - Creare Catalog produse
#Radu Catalina


class Catalog:
    ''' Se creaza clasa parinte pentru Electrocasnice mari si Electrocasnice mici_'''

    lista_obiecte = []
    clasa = ""
    subclasa = ""

    def __init__(self, pret, consum, producator, cod_produs):
        self.pret = pret
        self.consum = consum
        self.producator = producator
        self.cod_produs = cod_produs
        Catalog.lista_obiecte.append(self)


    def sortare_dupa_pret (self):
        for obj in sorted(Catalog.lista_obiecte, key=lambda element_lista:element_lista.pret):
            print ('**********************')
            print (f'Nume {obj.producator}')
            print ("Pret", {obj.pret})
            print(Catalog.clasa)
            print(Catalog.subclasa)

    def sortare_dupa_consum(self):
        for obj in sorted(Catalog.lista_obiecte, key=lambda element_lista:element_lista.consum):
            print ('**********************')
            print (f'Nume {obj.producator}')
            print ("Consum", {obj.consum})
            print(Catalog.clasa)
            print(Catalog.subclasa)

    def afisare_dupa_producator(self, producator):
        self.producator = input('Introduceti producatorul dorit:')
        for obj in [obj for obj in Catalog.lista_obiecte if producator.lower == obj.producator.lower()]:
            if obj.producator == producator:
                print(producator)


class Electrocasnice_mari(Catalog):
    def __init__(self, pret, consum, producator, cod_produs, adancime, latime, inaltime):
        super().__init__(pret, consum, producator, cod_produs)
        self.adancime = adancime
        self.latime = latime
        self.inaltime = inaltime


class Electrocasnice_mici(Catalog):
    def __init__(self, pret, consum, producator, cod_produs, lungime_cablu, baterie):
        super().__init__(pret, consum, producator, cod_produs)
        self.lungime_cablu = lungime_cablu
        self.baterie = baterie


class Frigider(Electrocasnice_mari):
    def __init__(self, pret, consum, producator, cod_produs, adancime, latime, inaltime, capacitate_congelator,
                 capacitate_frigider):
        super().__init__(pret, consum, producator, cod_produs, adancime, latime, inaltime)
        self.capacitate_congelator = capacitate_congelator
        self.capacitate_frigider = capacitate_frigider
        Catalog.clasa = 'Electrocasnice_mari'
        Catalog.subclasa = 'Frigider'


class Aragaz(Electrocasnice_mari):
    def __init__(self, pret, consum, producator, cod_produs, adancime, latime, inaltime, nr_arzatoare):
        super().__init__(pret, consum, producator, cod_produs, adancime, latime, inaltime)
        self.nr_arzatoare = nr_arzatoare
        Catalog.clasa = 'Electrocasnice_mari'
        Catalog.subclasa = 'Aragaz'


class Mixer(Electrocasnice_mici):
    def __init__(self, pret, consum, producator, cod_produs, lungime_cablu, baterie, rotatii_min):
        super().__init__(pret, consum, producator, cod_produs, lungime_cablu, baterie)
        self.rotatii_min = rotatii_min
        Catalog.clasa = 'Electrocasnice_mici'
        Catalog.subclasa = 'Mixer'


class Fier_calcat(Electrocasnice_mici):
    def __init__(self, pret, consum, producator, cod_produs, lungime_cablu, baterie, rezervor):
        super().__init__(pret, consum, producator, cod_produs, lungime_cablu, baterie)
        self.rezervor = rezervor
        Catalog.clasa = 'Electrocasnice_mici'
        Catalog.subclasa = 'Fier calcat'


f1 = Frigider(1200, 226, 'Arctic', 'F01', 60, '54cm', 146.5, 46, 41)
Frigider(765, 225, 'Heinner', 'F02', 54, '55 cm', 143.5, 164, 47)
Aragaz(1449, 674, 'Beko', 'A01', 60, 50, 88, 4)
Aragaz(771, 456, 'Arctic', 'A02', 50, 50, 85, 4)
Mixer(119, 300, 'Star Light', 'M01', 87, 'priza', '1000 rp')
Mixer(200, 400, 'Philips', 'M02', 87, 'priza', '950 rp')
Fier_calcat(59, 200, 'Tefal', 'FC01', 1.9, 'priza', 0.3)
Fier_calcat(239, 2600, 'Philips', 'FC02', 2, 'priza', 0.4)

print('\tCatalog produse\n')
print('''
    Selectati o optiune:
    1 - Afiseaza dupa pret 
    2 - Sorteaza dupa consum
    3 - Afiseaza dupa producator ''')

optiune = int(input('\nVa rugam selectati optiunea dorita din Catalog\n'))
if optiune == 1:
    f1.sortare_dupa_pret()
elif optiune == 2:
    f1.sortare_dupa_consum()
elif optiune == 3:
    f1.afisare_dupa_producator()
else:
    print('Va rugam selectati un numar intre 1 si 3')
