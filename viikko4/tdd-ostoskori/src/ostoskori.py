from tuote import Tuote
from ostos import Ostos
from functools import reduce

class Ostoskori:
    def __init__(self):
        self.kori=[]

        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
    def etsi_tuote_korista(self, nimi):
        index=None
        for i in range(len(self.kori)):
            if self.kori[i].tuotteen_nimi()==nimi:
                index=i
        return index

    def tavaroita_korissa(self):
        maara=0
        for ostos in self.kori:
            maara+=ostos.lukumaara()
        return maara
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        hinta=0
        for ostos in self.kori:
            hinta+=ostos.hinta()
        return hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        index=self.etsi_tuote_korista(lisattava.nimi())

        if index!=None:
            self.kori[index].muuta_lukumaaraa(1)
        else:
            ostos=Ostos(lisattava)
            self.kori.append(ostos)

    def poista_tuote(self, poistettava: Tuote):
        index=self.etsi_tuote_korista(poistettava.nimi())
        self.kori[index].muuta_lukumaaraa(-1)
        if self.kori[index].lukumaara()==0:
            self.kori.remove(self.kori[index])
        

    def tyhjenna(self):
        self.kori=[]
        # tyhjentää ostoskorin

    def ostokset(self):

        return self.kori
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
