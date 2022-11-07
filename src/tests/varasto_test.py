import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        #self.varasto = Varasto(10)
        #self.tester = Varasto(-1,-2)

    def test_negatiivinen_poisto(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-1),0)
    
    def test_negatiivinen_tilavuus(self):
        self.assertAlmostEqual(self.tester.tilavuus, 0)

    def test_negatiivinen_saldo(self):
        self.assertAlmostEqual(self.tester.saldo, 0)
        
    def test_lisaa_negatiivinen(self):
        self.varasto.lisaa_varastoon(-2)
        self.assertAlmostEqual(self.varasto.saldo,0)

    def test_str(self):
        self.assertEqual(self.varasto.__str__(), "saldo = 0, vielä tilaa 10")

    def test_saldo_tilavuus(self):
        self.test = Varasto(1, alku_saldo = 2)
        self.assertAlmostEqual(self.test.saldo, 1)

    def test_lisaa_liikaa(self):
        self.varasto.lisaa_varastoon(11)
        self.assertAlmostEqual(self.varasto.saldo,10)

    def test_ota_tyhjasta_varastosta(self):
        self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
