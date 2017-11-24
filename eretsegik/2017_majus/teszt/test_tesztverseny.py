#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from unittest.mock import patch
from tesztverseny_testable import *


class TesztversenyTestCase(unittest.TestCase):

    def setUp(self):
        self.megoldas, self.valaszok = feladat1()

    def testFeladat2(self):
        self.assertEqual(feladat2(self.valaszok), 303)

    @patch('builtins.input', lambda be: 'AB123')
    def testFeladat3(self):
        self.assertEqual(feladat3(self.valaszok), "BXCDBBACACADBC")

    def testFeladat4(self):
        self.assertListEqual(feladat4("BXCDBBACACADBC", self.megoldas), [
                             "+", " ", "+", " ", " ", "+", " ", " ", " ", "+", " ", " ", " ", " "])

    @patch('builtins.input', lambda be: '10')
    def testFeladat5(self):
        helyes, szazalek = feladat5(self.megoldas, self.valaszok)
        self.assertEqual(helyes, 111)
        self.assertEqual(szazalek, 36.63)

    def testFeladat6(self):

        helyes = {}

        with open("pontok_helyes.txt") as f:
            lines = f.read().splitlines()
            for line in lines:
                azon, valasz = line.split(" ")
                helyes[azon] = int(valasz)

        tesztelendo = feladat6(self.megoldas, self.valaszok)

        for sor in tesztelendo:
            self.assertEqual(sor[1], helyes[sor[0]], "Hiba: (" + sor[0] + ")")

    def testFeladat7(self):
        ertekeles = feladat6(self.megoldas, self.valaszok)

        nyertesek_tesztelendo = feladat7(ertekeles)

        helyes = {
            "JO001": 1,
            "DG490": 2,
            "UA889": 2,
            "FX387": 3
        }

        for nyertes in nyertesek_tesztelendo:
            self.assertEqual(nyertes[0], helyes[nyertes[1]],
                             nyertes[1] + " - " + str(helyes[nyertes[1]]))


def main():
    unittest.main(verbosity=2)


if __name__ == '__main__':
    main()
