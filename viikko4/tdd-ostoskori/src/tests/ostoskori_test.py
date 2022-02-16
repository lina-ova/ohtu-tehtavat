import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
    
    def test_tavaroita_korissa_aluksi_nolla(self):
        self.assertEqual(self.kori.tavaroita_korissa(),0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_sama_kuin_tuotteen(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(),3)
    def test_kahden_tuotteen_lisaamisen_jalkeen_korin_hinta_sama_kuin_summa(self):
        maito = Tuote("Maito", 3)
        sokeri=Tuote('Sokeri',2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(sokeri)
        self.assertEqual(self.kori.hinta(),5)
    
    def test_kahden_tuotteen_lisaamisen_jalkeen_korissa_on_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        sokeri=Tuote('Sokeri',2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(sokeri)
        self.assertEqual(self.kori.tavaroita_korissa(),2)
    
    def test_kaksi_samaa_tuotetta_hinta_oikein(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(),3*2)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
 
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(),'Maito')
        self.assertEqual(ostos.lukumaara(),1)
