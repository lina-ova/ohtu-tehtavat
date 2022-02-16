import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.maito=Tuote("Maito", 3)
        self.sokeri=Tuote('Sokeri',2)

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
    
    def test_tavaroita_korissa_aluksi_nolla(self):
        self.assertEqual(self.kori.tavaroita_korissa(),0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(self.maito)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_sama_kuin_tuotteen(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.hinta(),3)

    def test_kahden_tuotteen_lisaamisen_jalkeen_korin_hinta_sama_kuin_summa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.sokeri)
        self.assertEqual(self.kori.hinta(),5)
    
    def test_kahden_tuotteen_lisaamisen_jalkeen_korissa_on_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.sokeri)
        self.assertEqual(self.kori.tavaroita_korissa(),2)
    
    def test_kaksi_samaa_tuotetta_hinta_oikein(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.hinta(),3*2)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        self.kori.lisaa_tuote(self.maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        self.kori.lisaa_tuote(self.maito)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(),'Maito')
        self.assertEqual(ostos.lukumaara(),1)
    
    def test_kahden_tuotteen_lisaamisen_jalkeen_korissa_on_kaksi_ostosoliota(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.sokeri)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset),2)
