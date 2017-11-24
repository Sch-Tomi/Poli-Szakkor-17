#!/usr/bin/python
# -*- coding: utf-8 -*-


def feladat1():
    naplo = {}
    bejegyzesek = 0

    f = open("naplo.txt")
    sorok = f.read().splitlines()
    f.close()

    datum = None

    for sor in sorok:
        felbontott = sor.split(" ")

        if felbontott[0][0] == "#":
            datum = felbontott[1] + "." + felbontott[2]
            naplo[datum] = []
        else:
            naplo[datum].append(
                {"nev": felbontott[0] + " " + felbontott[1], "hianyzas": felbontott[2]})
            bejegyzesek += 1

    return (naplo, bejegyzesek)


def feladat2(bejegyzesek):
    print("2. feladat:")
    print("A naplóban", bejegyzesek, "bejegyzés van.\n")


def feladat3(naplo):

    igazolt = 0
    igazolatlan = 0

    for nap in naplo.values():
        for ember in nap:
            for jelzes in ember["hianyzas"]:
                if jelzes == "X":
                    igazolt += 1
                elif jelzes == "I":
                    igazolatlan += 1

    print("3. feladat:")
    print("Az igazolt hiányzások száma", igazolt,
          ", az igazolatlanoké", igazolatlan, "óra.\n")


def hetnapja(honap: int, nap: int) -> str:
    napnev = ["vasarnap", "hetfo", "kedd",
              "szerda", "csutortok", "pentek", "szombat"]
    napszam = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335]
    napsorszam = (napszam[honap - 1] + nap) % 7
    return napnev[napsorszam]


def feladat5():
    print("5. feladat:")
    honap = int(input("A hónap sorszáma: "))
    nap = int(input("A nap sorszáma: "))

    print("Azon a napon", hetnapja(honap, nap), "volt.\n")


def feladat6(naplo):

    print("6. feladat:")
    valasztott_nap = input("A nap neve: ")
    valasztott_ora = int(input("Az óra sorszáma: "))
    hianyzasok = 0

    for datum in naplo.keys():
        honap = int(datum.split(".")[0])
        nap = int(datum.split(".")[1])

        if hetnapja(honap, nap) == valasztott_nap:
            for ember in naplo.get(datum):
                if ember["hianyzas"][valasztott_ora - 1] == "X":
                    hianyzasok += 1
                elif ember["hianyzas"][valasztott_ora - 1] == "I":
                    hianyzasok += 1

    print("Ekkor összesen", hianyzasok, "óra hiányzás történt.")


def feladat7(naplo):

    hianyzasok = {}

    for datum in naplo.keys():
        for ember in naplo.get(datum):
            hianyzas = 0
            for jelzes in ember["hianyzas"]:
                if jelzes == "X":
                    hianyzas += 1
                elif jelzes == "I":
                    hianyzas += 1

            if ember["nev"] in hianyzasok.keys():
                hianyzasok[ember["nev"]] += hianyzas
            else:
                hianyzasok[ember["nev"]] = hianyzas

    legtobb = max(hianyzasok.values())
    legtobbet_hianyzok = []

    for nev in hianyzasok.keys():
        if hianyzasok.get(nev) == legtobb:
            legtobbet_hianyzok.append(nev)

    print("7. feladat:")
    print("A legtöbbet hiányzó tanulók:")
    print(*legtobbet_hianyzok)


if __name__ == '__main__':
    naplo, bejegyzesek = feladat1()
    feladat2(bejegyzesek)
    feladat3(naplo)
    feladat5()
    feladat6(naplo)
    feladat7(naplo)
