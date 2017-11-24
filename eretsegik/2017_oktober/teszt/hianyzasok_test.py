#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from unittest.mock import patch
from hianyzasok import *


class HianyzasokTestCase(unittest.TestCase):

    def setUp(self):
        self.naplo, self.bejegyzesek = feladat1()

    def testFeladat2(self):
        self.assertEqual(self.bejegyzesek, 139)

    def testFeladat3(self):
        igazolt, igazolatlan = feladat3(self.naplo)

        self.assertEqual(igazolt, 788, "Igazolt téves")
        self.assertEqual(igazolatlan, 18, "Igazolatlan téves")

    def testFeladat5(self):
        self.assertEqual(hetnapja(1, 1), "hetfo")
        self.assertEqual(hetnapja(2, 3), "szombat")

    def testFeladat6(self):
        with patch('builtins.input', side_effect=["szerda", 3]):
            self.assertEqual(feladat6(self.naplo), 49)

    def testFeladat7(self):
        self.assertCountEqual(feladat7(self.naplo), [
                              "Kivi Adrienn", "Jujuba Ibolya"])


def main():
    unittest.main(verbosity=2)


if __name__ == '__main__':
    main()
