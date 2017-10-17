#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint

titok = randint(1,100)

kitalalva = False

while not kitalalva:

    tipp = input("Tipped: ")

    if tipp == "exit":
        kitalalva = True
    else:
        tipp = int(tipp) # most már szám...

        if tipp < titok:
            print("Nagyobbra gondoltam")
        elif  tipp > titok:
            print("Kissebbre gondoltam")
        else:
            print("Eltaláltad!")
            kitalalva = True