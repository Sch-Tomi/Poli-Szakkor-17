#!/usr/bin/python
# -*- coding: utf-8 -*-


class Item:

    def __init__(self):
        self.bonusStr = 0
        self.bonusAgi = 0
        self.bonusInt = 0
        self.armor = 0
        self.hpRegen = 0
        self.bonusDmg = 0

    def add_bonusStr(self, bonusStrength):
        self.bonusStr += bonusStrength

    def add_bonusAgi(self, bonusAgility):
        self.bonusAgi += bonusAgility

    def add_bonusInt(self, bonusInteligence):
        self.bonusInt += bonusInteligence

    def add_bonusDmg(self, bonusDmg):
        self.bonusDmg += bonusDmg

    def add_armor(self, armor):
        self.armor += armor

    def add_hpRegen(self, hpRegen):
        self.hpRegen += hpRegen

    def get_bonusStr(self):
        return self.bonusStr

    def get_bonusAgi(self):
        return self.bonusAgi

    def get_bonusInt(self):
        return self.bonusInt

    def get_bonusDmg(self):
        return self.get_bonusDmg

    def get_armor(self):
        return self.armor

    def get_hpRegen(self):
        return self.hpRegen

    def info(self):
        return "+Strength: {}\n+Agility: {}\n+Inteligence: {}\n+Damage: {}\n+Armor: {}\n+HP Regen: {}".format(
            self.bonusStr, self.bonusAgi, self.bonusInt, self.bonusDmg, self.armor, self.hpRegen)
