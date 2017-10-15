#!/usr/bin/python
# -*- coding: utf-8 -*-

kitalalando = 42 

tipp = int(input("Tippelj egy számot: "))

if kitalalando < tipp:
    print("Ennél kissebbre gondoltam!")
elif kitalalando > tipp:
    print("Ennél nagyobbra gondoltam!")
else:
    print("Eltaláltad")