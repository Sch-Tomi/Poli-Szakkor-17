#!/usr/bin/python
# -*- coding: utf-8 -*-


def feladat1():

    print("1. feladat: Az adatok beolvasása\n")

    f = open("valaszok.txt")
    megoldas = f.readline().strip()
    valaszok = f.read().splitlines()
    f.close()

    return (megoldas, valaszok)


def feladat2(valaszok):

    print("2. feladat: A vetélkedőn ", len(valaszok), " versenyző indult.\n")


def feladat3(valaszok):

    print("3. feladat:")

    azon = input("A versenyző azonosítója: ")
    keresett = None

    for sor in valaszok:
        valasz = sor.split(" ")
        if valasz[0] == azon:
            keresett = valasz[1]
            break

    print(azon, " válasza: ", keresett, "\n")

    return keresett


def feladat4(valasz, megoldas):
    print("4. feladat:")

    ell = []

    for i in range(len(valasz)):
        if valasz[i] == megoldas[i]:
            ell.append("+")
        else:
            ell.append(" ")

    print(megoldas, "    ", "(a helyes megoldás)")
    print(*ell, sep='', end='')
    print("     ", "(a versenyző helyes válaszai)\n")


def feladat5(megoldas, valaszok):

    print("5. feladat:")

    feladat = int(input("A feladat sorszáma: ")) - 1

    helyes = 0

    for sor in valaszok:
        valasz = sor.split(" ")[1]
        if valasz[feladat] == megoldas[feladat]:
            helyes += 1

    szazalek = round(helyes / len(valaszok) * 100, 2)

    print("A feladatra", helyes, "fő, a versenyzők ",
          szazalek, "%-a adott helyes választ.\n")


def feladat6(megoldas, valaszok):

    print("6. feladat: A versenyzők pontszámának meghatározása\n")

    ertekelesek = []

    for valasz in valaszok:
        azon, tipp = valasz.split(" ")
        pont = 0

        for i in range(0, 5):
            if tipp[i] == megoldas[i]:
                pont += 3

        for i in range(5, 10):
            if tipp[i] == megoldas[i]:
                pont += 4

        for i in range(10, 13):
            if tipp[i] == megoldas[i]:
                pont += 5

        if tipp[13] == megoldas[13]:
            pont += 6

        ertekelesek.append([azon, pont])

    f = open("pontok.txt", "w")
    for ertekeles in ertekelesek:
        f.write(str(ertekeles[0]) + " " + str(ertekeles[1]) + "\n")
    f.close()

    return ertekelesek


def feladat7(ertekelesek):

    print("7. feladat: A verseny legjobbjai: ")

    legjobbak = []

    pontok = [ertekeles[1] for ertekeles in ertekelesek]

    for i in range(0, 3):
        if len(pontok) > 0:

            maxi = max(pontok)

            legjobbak.append(maxi)

            while maxi in pontok:
                pontok.remove(maxi)

    for i in range(len(legjobbak)):
        for ertekeles in ertekelesek:
            if ertekeles[1] == legjobbak[i]:
                print(str(i + 1) + ". díj (" +
                      str(legjobbak[i]) + " pont): " + ertekeles[0])


if __name__ == '__main__':

    megoldas, valaszok = feladat1()

    feladat2(valaszok)
    keresett_valasz = feladat3(valaszok)
    feladat4(keresett_valasz, megoldas)
    feladat5(megoldas, valaszok)
    ertekelesek = feladat6(megoldas, valaszok)
    feladat7(ertekelesek)
