#!/usr/bin/python
# -*- coding: utf-8 -*-

import random


class Ability:

    strength = None
    agility = None
    intelligence = None

    def __init__(self, strength, agility, intelligence):
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence


class Warrior:

    name = None
    heatlh = None
    ability = None
    weapon = None
    shield = None

    def __init__(self, name, heatlh, ability, weapon, shield):
        self.name = name
        self.heatlh = heatlh
        self.ability = ability
        self.weapon = weapon
        self.shield = shield

    def fight(self):
        return self.weapon.hit(self.ability)

    def suffer(self, hitPoint):
        if self.shield.tryToBlock(self.ability):
            print("Hahahah, I parry your blow!(" +
                  self.name + ", " + str(self.heatlh) + ")")
        else:
            self.heatlh -= hitPoint
            print("Ahh, I suffered", hitPoint, "damage!(" +
                  self.name + ", " + str(self.heatlh) + ")")

    def isAlive(self):
        return self.heatlh > 0


class Weapon:

    hitPoint = None

    def __init__(self, hitPoint):
        self.hitPoint = hitPoint

    def hit(self, ability):
        return self.hitPoint


class Sceptre(Weapon):
    def __init__(self, hitPoint):
        super().__init__(hitPoint)

    def hit(self, ability):

        bonus = 0

        if random.randint(1, 100) > 85:
            bonus = 100

        return (ability.agility * 0.25) * (ability.intelligence * 0.7) * self.hitPoint + bonus


class WarHammer(Weapon):
    def __init__(self, hitPoint):
        super().__init__(hitPoint)

    def hit(self, ability):

        bonus = 0

        if random.randint(1, 100) > 70:
            bonus = 20

        return (ability.agility * 0.25) * (ability.strength * 0.5) * self.hitPoint + bonus


class Shield:

    chance = None

    def __init__(self, chance_to_block):
        self.chance = chance_to_block

    def tryToBlock(self, ability):
        if random.randint(1, 100) > (100 - self.chance + (ability.agility * 0.5)):
            return True

        return False


def main():

    glowstick_of_destiny = Sceptre(2)
    mjolnir = WarHammer(10)

    america_captain_shield = Shield(70)
    no_shield = Shield(10)

    loki = Warrior("Loki", 5000, Ability(10, 10, 30),
                   glowstick_of_destiny, no_shield)
    thor = Warrior("Thor", 10000, Ability(50, 30, 10),
                   mjolnir, america_captain_shield)

    while loki.isAlive() and thor.isAlive():
        thor.suffer(loki.fight())
        loki.suffer(thor.fight())

    if loki.isAlive():
        print("Loki is the winner! God save the world!")
    elif thor.isAlive():
        print("Thor saved ur ass!")
    else:
        print("ehhh, what was that?!")


if __name__ == '__main__':
    main()
