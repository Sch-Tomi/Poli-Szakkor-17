#!/usr/bin/python
# -*- coding: utf-8 -*-

muveletek = ["+", "-", "*", "/"]
fut = True
kilepoSzo = "EXIT"

clear = True



while fut:
    
    if clear:
        a = int(input(""))
        clear = False
    else:
        print(a)
    
    muvelet = input("")
    b = int(input(""))

    if a == kilepoSzo or muvelet == kilepoSzo or b == kilepoSzo:
        fut = False
        break

    if muvelet == "C" or b == "C":
        clear = True
        a = 0
        b = 0
        muvelet = ""


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
    print("----")
    print(a)
    print("\n\n")