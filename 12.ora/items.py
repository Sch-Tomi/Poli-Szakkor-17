#!/usr/bin/python
# -*- coding: utf-8 -*-

from item import Item

class ChainMail(Item):
    def __init__(self):
        super().__init__()
        self.add_armor(5)

class PlateMail(Item):
    def __init__(self):
        super().__init__()
        self.add_armor(10)

class AssaultCuirass(ChainMail, PlateMail):
    def __init__(self):
        super().__init__()

class BroadSword(Item):
    def __init__(self):
        super().__init__()
        self.add_bonusDmg(18)

class RobeOfTheMagi(Item):
    def __init__(self):
        super().__init__()
        self.add_bonusInt(6)

class BladeMail(ChainMail, BroadSword, RobeOfTheMagi):
    def __init__(self):
        super().__init__()

class BladesOfAttack(Item):
    def __init__(self):
        super().__init__()
        self.add_bonusDmg(9)

class Crystalys(BroadSword, BladesOfAttack):
    def __init__(self):
        super().__init__()

class RingOfHealth(Item):
    def __init__(self):
        super().__init__()
        self.add_hpRegen(5)

class RingOfRegen(Item):
    def __init__(self):
        super().__init__()
        self.add_hpRegen(1.5)

class Cloak(Item):
    def __init__(self):
        super().__init__()
        self.add_armor(2)

class HoodOfDefiance(RingOfRegen, RingOfHealth, Cloak):
    def __init__(self):
        super().__init__()