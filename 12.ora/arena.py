#!/usr/bin/python
# -*- coding: utf-8 -*-

from items import *
from hero import Hero

class Arena:

    def __init__(self):
       self.__heroes = [self.__hero1(), self.__hero2()]

    def __hero1(self):
        hero1 = Hero("Jozsi", 10, 10, 10, 10)
        hero1.add_item(ChainMail())
        return hero1

    def __hero2(self):
        hero2 = Hero("Pista", 20, 10, 10, 20)
        hero2.add_item(ChainMail())
        return hero2

    def fight(self):
        
        self.report()
        while self.__heroes[0].isAlive() and self.__heroes[1].isAlive():
            self.__heroes[0].hit(self.__heroes[1])
            self.__heroes[1].hit(self.__heroes[0])

            self.report()

    def report(self):
        print("------------------")
        for hero in self.__heroes:
            print("Name: {}, health: {}".format( hero.name, hero.hp))
    
def main():
    Arena().fight()

if __name__ == '__main__':
    main()