#!/usr/bin/python
# -*- coding: utf-8 -*-

import simpleaudio as sa
from time import sleep

hangjegyek = ["c1", "d1", "e1", "f1", "g1", "a1", "b1", "c2"]

hangok = {}

for hangjegy in hangjegyek:
    hangok[hangjegy] = sa.WaveObject.from_wave_file("wav/"+hangjegy+".wav")

zenefile = input("Add meg a zene fájlt: ")

f = open(zenefile)
f_tartalom = f.read()
f.close()

for f_hangjegy in f_tartalom.split(" "):
    if f_hangjegy == "z":
        sleep(0.5)
    else:
        hangok[f_hangjegy].play().wait_done()
        
    