#!/usr/bin/python
# -*- coding: utf-8 -*-

muveletek = ["+", "-", "*", "/"]
fut = True
kilepoSzo = "EXIT"

while fut:
    a = int(input(""))
    muvelet = input("")
    b = int(input(""))

    if a == kilepoSzo or muvelet == kilepoSzo or b == kilepoSzo:
        fut = False
        break

    if muvelet in muveletek:
        if muvelet == "+":
            print(a+b)
        elif muvelet == "-":
            print(a-b)
        elif muvelet == "*":
            print(a*b)
        elif muvelet == "/":
            if b == 0:
                print("0-val nem osztunk!")
            else:
                print(a/b)
