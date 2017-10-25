#!/usr/bin/python
# -*- coding: utf-8 -*-


lista = [730257, 203073, 94979, 465113, 966344]

maximum = lista[0]

for elem in lista:
   if elem > maximum: # itt kell kicserélni <-ra ha minimumot akarsz keresni
       maximum = elem

print(maximum)