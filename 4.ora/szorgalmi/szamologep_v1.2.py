#!/usr/bin/python
# -*- coding: utf-8 -*-

muveletek = ["+", "-", "*", "/"]

a = int(input(""))
muvelet = input("")
b = int(input(""))


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
