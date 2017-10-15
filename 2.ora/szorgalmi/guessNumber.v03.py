#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint

kitalalando = randint(1, 100)

tipp = int(input("Tippelj egy számot: "))

if kitalalando < tipp:
    print("Ennél kissebbre gondoltam!")
elif kitalalando > tipp:
    print("Ennél nagyobbra gondoltam!")
else:
    print("Eltaláltad")
