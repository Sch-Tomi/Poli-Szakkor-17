#!/usr/bin/python
# -*- coding: utf-8 -*-


lista = [730257, 203073, 94979, 465113, 966344]

keresett_elem = None

for elem in lista:
   if elem % 2 == 0:
       keresett_elem = elem
       break


print(keresett_elem)