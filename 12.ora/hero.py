#!/usr/bin/python
# -*- coding: utf-8 -*-


class Hero:

    def __init__(self,name, strength, agility, inteligence, dmg):
        self.name = name
        
        self.baseStrength = strength
        self.baseAgility = agility
        self.baseInteligence = inteligence
        self.baseDmg = dmg

        self.strength = strength
        self.agility = agility
        self.inteligence = inteligence
        self.dmg = dmg

        self.maxHp = 0
        self.hp = 0
        self.hpRegen = 0

        self.armor = 0

        self.inventory = []

        self.__recalcStats()
        self.__regenToMaxHP()

    def add_item(self, item):
        if len(self.inventory) <= 6:
            self.inventory.append(item)

    def isAlive(self):
        return self.hp > 0

    def hit(self, enemy):
        enemy.suffer(self.dmg)
    
    def suffer(self, incomingDmg):
        takenDmg = incomingDmg * (1 - 0.05 * self.armor / (1 + 0.05 * abs(self.armor)))
        self.hp -= takenDmg

    def __recalcStats(self):

        self.strength = self.baseStrength + self.__calcBonusStr()
        self.agility = self.baseAgility + self.__calcBonusAgi()
        self.inteligence = self.baseInteligence + self.__calcBonusInt()

        self.dmg = self.baseDmg + self.__calcBonusDmg()

        self.maxHp = self.__calcMaxHp()
        self.hpRegen = self.__calcMaxHpRegen() + self.__calcMaxHpRegen()
        self.armor = self.__calcArmor() + self.__calcBonusArmor()

    def __calcMaxHp(self):
        return 20 * self.strength

    def __calcMaxHpRegen(self):
        return 0.03 * self.strength

    def __calcArmor(self):
        return 0.14 * self.agility

    def __calcBonusStr(self):
        bonus = 0
        for item in self.inventory:
            bonus += item.get_bonusStr()
        return bonus
    
    def __calcBonusAgi(self):
        bonus = 0
        for item in self.inventory:
            bonus += item.get_bonusAgi()
        return bonus
    
    def __calcBonusInt(self):
        bonus = 0
        for item in self.inventory:
            bonus += item.get_bonusInt()
        return bonus
    
    def __calcBonusArmor(self):
        bonus = 0
        for item in self.inventory:
            bonus += item.get_armor()
        return bonus
    
    def __calcBonusHpRegen(self):
        bonus = 0
        for item in self.inventory:
            bonus += item.get_hpRegen()
        return bonus

    def __calcBonusDmg(self):
        bonus = 0
        for item in self.inventory:
            bonus += item.get_bonusDmg()
        return bonus    

    def __regenToMaxHP(self):
        self.hp = self.maxHp
    