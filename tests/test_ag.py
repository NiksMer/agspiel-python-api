#  Copyright (c) 2020 | KingKevin23 (@kingkevin023)

from unittest import TestCase
from datetime import datetime
from agspiel.api.ag import Ag
from agspiel.api.ceo import Ceo
from agspiel.api.aktie import Aktie
from agspiel.api.anleihe import Anleihe, Kredit
from agspiel.api.zertifikat import Zertifikat
from agspiel.api.order import Order

class TestAg(TestCase):
    def setUp(self):
        ceo = {"name":"KingKevin23", "registrierung_datum":"2020-02-04 16:24:00", "gesperrt":"false", "ist_userprojekt_account":"false"}
        aktien = [{"wkn":"104531", "stueckzahl":"146"}, {"wkn":"105516", "stueckzahl":"23"}]
        anleihen = [{"betrag":"10000000", "zins":"0.32", "auszahlung_datum":"2020-08-14 15:01:33", "laufzeit":"5"}]
        kredite = [{"betrag":"10000000", "zins":"0.32", "rueckzahlung_datum":"2020-08-14 15:01:33", "laufzeit":"5"}]
        zertifikate = [{"betrag":"234.43", "typ":"call", "hebel":"1.092", "punkte":"23443", "ablauf_datum":"2020-08-10 17:48:01"}]
        orders = [{"typ":"sell", "limit":"410", "stueckzahl":"303", "orderregel":"false", "systembank_order":"false", "datum":"2020-08-10 01:21:35"}]
        api_data = {"wkn":"175353", "name":"King Kompany", "gruendung":"2020-02-04 16:25:05", "aktienanzahl":"2000000",
                    "in_liquidation":"false", "kurs":"338.68", "brief":"338.68", "brief_stueckzahl":"117391", "geld":"0",
                    "geld_stueckzahl":"0", "depotwert":"162516884.99", "bargeld":"5378562.51", "highscore_platz":"528",
                    "highscore_platz_groesse":"337", "highscore_platz_wachstum":"502", "highscore_platz_newcomer":"0",
                    "agsx_punkte":"1026", "in_agsx":"false", "handelsaktivitaet":"42", "ceo":ceo, "aktien":aktien,
                    "anleihen":anleihen, "kredite":kredite, "zertifikate":zertifikate, "orders":orders}
        self.ag = Ag(api_data=api_data, web_data="")

    def test_wkn(self):
        self.assertEqual(self.ag.wkn, 175353)
        self.assertIsInstance(self.ag.wkn, int)

    def test_name(self):
        self.assertEqual(self.ag.name, "King Kompany")
        self.assertIsInstance(self.ag.name, str)

    def test_gruendung(self):
        self.assertEqual(self.ag.gruendung, datetime(year=2020, month=2, day=4, hour=16, minute=25, second=5))
        self.assertIsInstance(self.ag.gruendung, datetime)

    def test_aktienanzahl(self):
        self.assertEqual(self.ag.aktienanzahl, 2000000)
        self.assertIsInstance(self.ag.aktienanzahl, int)

    def test_in_liquidation(self):
        self.assertEqual(self.ag.in_liquidation, False)
        self.assertIsInstance(self.ag.in_liquidation, bool)

    def test_kurs(self):
        self.assertEqual(self.ag.kurs, 338.68)
        self.assertIsInstance(self.ag.kurs, float)

    def test_brief(self):
        self.assertEqual(self.ag.brief, 338.68)
        self.assertIsInstance(self.ag.brief, float)

    def test_geld(self):
        self.assertEqual(self.ag.geld, 0)
        self.assertIsInstance(self.ag.geld, float)

    def test_brief_stueckzahl(self):
        self.assertEqual(self.ag.brief_stueckzahl, 117391)
        self.assertIsInstance(self.ag.brief_stueckzahl, int)

    def test_geld_stueckzahl(self):
        self.assertEqual(self.ag.geld_stueckzahl, 0)
        self.assertIsInstance(self.ag.geld_stueckzahl, int)

    def test_depotwert(self):
        self.assertEqual(self.ag.depotwert, 162516884.99)
        self.assertIsInstance(self.ag.depotwert, float)

    def test_bargeld(self):
        self.assertEqual(self.ag.bargeld, 5378562.51)
        self.assertIsInstance(self.ag.bargeld, float)

    def test_highscore(self):
        self.assertEqual(self.ag.highscore, 528)
        self.assertIsInstance(self.ag.highscore, int)

    def test_highscore_groesse(self):
        self.assertEqual(self.ag.highscore_groesse, 337)
        self.assertIsInstance(self.ag.highscore_groesse, int)

    def test_highscore_wachstum(self):
        self.assertEqual(self.ag.highscore_wachstum, 502)
        self.assertIsInstance(self.ag.highscore_wachstum, int)

    def test_highscore_newcomer(self):
        self.assertEqual(self.ag.highscore_newcomer, 0)
        self.assertIsInstance(self.ag.highscore_newcomer, int)

    def test_agsx_punkte(self):
        self.assertEqual(self.ag.agsx_punkte, 1026)
        self.assertIsInstance(self.ag.agsx_punkte, int)

    def test_in_agsx(self):
        self.assertEqual(self.ag.in_agsx, False)
        self.assertIsInstance(self.ag.in_agsx, bool)

    def test_handelsaktivitaet(self):
        self.assertEqual(self.ag.handelsaktivitaet, 42)
        self.assertIsInstance(self.ag.handelsaktivitaet, int)

    def test_ceo(self):
        self.assertIsInstance(self.ag.ceo, Ceo)
        self.assertEqual(self.ag.ceo.name, "KingKevin23")
        self.assertIsInstance(self.ag.ceo.name, str)
        self.assertEqual(self.ag.ceo.registrierung_datum, datetime(year=2020, month=2, day=4, hour=16, minute=24))
        self.assertIsInstance(self.ag.ceo.registrierung_datum, datetime)
        self.assertEqual(self.ag.ceo.gesperrt, False)
        self.assertIsInstance(self.ag.ceo.gesperrt, bool)
        self.assertEqual(self.ag.ceo.userprojekt, False)
        self.assertIsInstance(self.ag.ceo.userprojekt, bool)

    def test_aktien(self):
        for i in self.ag.aktien:
            self.assertIsInstance(i, Aktie)
        self.assertEqual(self.ag.aktien[0].wkn, 104531)
        self.assertIsInstance(self.ag.aktien[0].wkn, int)
        self.assertEqual(self.ag.aktien[0].stueckzahl, 146)
        self.assertIsInstance(self.ag.aktien[0].stueckzahl, int)
        self.assertEqual(self.ag.aktien[1].wkn, 105516)
        self.assertIsInstance(self.ag.aktien[1].wkn, int)
        self.assertEqual(self.ag.aktien[1].stueckzahl, 23)
        self.assertIsInstance(self.ag.aktien[1].stueckzahl, int)

    def test_anleihen(self):
        for i in self.ag.anleihen:
            self.assertIsInstance(i, Anleihe)
        self.assertEqual(self.ag.anleihen[0].betrag, 10000000)
        self.assertIsInstance(self.ag.anleihen[0].betrag, int)
        self.assertEqual(self.ag.anleihen[0].zins, 0.32)
        self.assertIsInstance(self.ag.anleihen[0].zins, float)
        self.assertEqual(self.ag.anleihen[0].auszahlung_datum, datetime(year=2020, month=8, day=14, hour=15, minute=1, second=33))
        self.assertIsInstance(self.ag.anleihen[0].auszahlung_datum, datetime)
        self.assertEqual(self.ag.anleihen[0].laufzeit, 5)
        self.assertIsInstance(self.ag.anleihen[0].laufzeit, int)

    def test_kredite(self):
        for i in self.ag.kredite:
            self.assertIsInstance(i, Kredit)
        self.assertEqual(self.ag.kredite[0].betrag, 10000000)
        self.assertIsInstance(self.ag.kredite[0].betrag, int)
        self.assertEqual(self.ag.kredite[0].zins, 0.32)
        self.assertIsInstance(self.ag.kredite[0].zins, float)
        self.assertEqual(self.ag.kredite[0].rueckzahlung_datum, datetime(year=2020, month=8, day=14, hour=15, minute=1, second=33))
        self.assertIsInstance(self.ag.kredite[0].rueckzahlung_datum, datetime)
        self.assertEqual(self.ag.kredite[0].laufzeit, 5)
        self.assertIsInstance(self.ag.kredite[0].laufzeit, int)

    def test_zertifikate(self):
        for i in self.ag.zertifikate:
            self.assertIsInstance(i, Zertifikat)
        self.assertEqual(self.ag.zertifikate[0].betrag, 234.43)
        self.assertIsInstance(self.ag.zertifikate[0].betrag, float)
        self.assertEqual(self.ag.zertifikate[0].typ, "call")
        self.assertIsInstance(self.ag.zertifikate[0].typ, str)
        self.assertEqual(self.ag.zertifikate[0].hebel, 1.092)
        self.assertIsInstance(self.ag.zertifikate[0].hebel, float)
        self.assertEqual(self.ag.zertifikate[0].punkte, 23443)
        self.assertIsInstance(self.ag.zertifikate[0].punkte, int)
        self.assertEqual(self.ag.zertifikate[0].ablaufdatum, datetime(year=2020, month=8, day=10, hour=17, minute=48, second=1))
        self.assertIsInstance(self.ag.zertifikate[0].ablaufdatum, datetime)

    def test_orders(self):
        for i in self.ag.orders:
            self.assertIsInstance(i, Order)
        self.assertEqual(self.ag.orders[0].typ, "sell")
        self.assertIsInstance(self.ag.orders[0].typ, str)
        self.assertEqual(self.ag.orders[0].limit, 410)
        self.assertIsInstance(self.ag.orders[0].limit, float)
        self.assertEqual(self.ag.orders[0].stueckzahl, 303)
        self.assertIsInstance(self.ag.orders[0].stueckzahl, int)
        self.assertEqual(self.ag.orders[0].orderregel, False)
        self.assertIsInstance(self.ag.orders[0].orderregel, bool)
        self.assertEqual(self.ag.orders[0].systembank, False)
        self.assertIsInstance(self.ag.orders[0].systembank, bool)
        self.assertEqual(self.ag.orders[0].datum, datetime(year=2020, month=8, day=10, hour=1, minute=21, second=35))
        self.assertIsInstance(self.ag.orders[0].datum, datetime)