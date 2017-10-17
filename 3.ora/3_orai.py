#!/usr/bin/python
# -*- coding: utf-8 -*-

szo = input("Adj meg egy szöveget!")

a_betuk_szama = 0

for betu in szo:
    if betu == "a":
        a_betuk_szama += 1

print("A betük száma a beadott szövegben: "+ str(a_betuk_szama))