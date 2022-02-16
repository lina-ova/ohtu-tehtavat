from tuote import Tuote
from ostos import Ostos


class Ostoskori:
    def __init__(self):
        self.kori=[]


    def etsi_tuote_korista(self, tuote: Tuote):
        for ostos in self.kori:
            if ostos.tuote==tuote:
                return ostos

        return None


    def tavaroita_korissa(self):
        maara=0
        for ostos in self.kori:
            maara+=ostos.lukumaara()
        return maara


    def hinta(self):
        hinta=0
        for ostos in self.kori:
            hinta+=ostos.hinta()
        return hinta


    def lisaa_tuote(self, lisattava: Tuote):
        ostos=self.etsi_tuote_korista(lisattava)

        if ostos!=None:
            ostos.muuta_lukumaaraa(1)
        else:
            ostos=Ostos(lisattava)
            self.kori.append(ostos)


    def poista_tuote(self, poistettava: Tuote):
        ostos=self.etsi_tuote_korista(poistettava)

        ostos.muuta_lukumaaraa(-1)

        if ostos.lukumaara()==0:
            self.kori.remove(ostos)
        

    def tyhjenna(self):
        self.kori=[]


    def ostokset(self):
        return self.kori

