#!/usr/bin/python
# -*- coding: utf-8 -*-

muveletek = ["+", "-", "*", "/"]
fut = True
kilepoSzo = "EXIT"

a = int(input(""))

while fut:
    
    muvelet = input("")
    b = int(input(""))

    if a == kilepoSzo or muvelet == kilepoSzo or b == kilepoSzo:
        fut = False
        break

    if muvelet in muveletek:
        if muvelet == "+":
            a = a+b
        elif muvelet == "-":
            a = a-b
        elif muvelet == "*":
            a = a*b
        elif muvelet == "/":
            if b == 0:
                print("0-val nem osztunk!")
                a = 0
            else:
                a = a/b
    
    print(a)