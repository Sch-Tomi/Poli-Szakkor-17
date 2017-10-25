#!/usr/bin/python
# -*- coding: utf-8 -*-


lista = [730257, 203073, 94979, 465113, 966344]

darab = 0

for elem in lista:
   if elem % 2 == 0: # itt bármilyen feltétel megadható természetesen nem csak az hogy páros-e
       darab = darab +1

print(darab)