 
def feladat1():

    print("1. feladat: Az adatok beolvasása ")

    fajl = open("valaszok.txt", "r")
    megoldas = fajl.readline().strip()
    valaszok = [] 

    for sor in fajl.readlines():
        valaszok.append(sor.strip().split(' '))

    return (valaszok, megoldas)

def feladat2(valaszok):
    print("2. feladat:")
    print("A vetélkedőn", len(valaszok) , "versenyző indult.")

def feladat3(valaszok):
    print("3. feladat:")
    keresettSzemely = input("Add meg az azonosítót: ")
    keresettValasz = None

    for valasz in valaszok:
        if valasz[0] == keresettSzemely:
            keresettValasz = valasz[1]
            print(valasz[1], "(a versenyző helyes válaszai)")
            break 

    return keresettValasz

def feladat4(megoldas, valasz):
    print("4. feladat:")

    pontozas = []

    for i in range(len(megoldas)):
        if megoldas[i] == valasz[i]:
            pontozas.append("+")
        else:
            pontozas.append(" ") 

    print(megoldas, "    ","(...)")
    print(*pontozas,sep='', end='')
    print("   ","(---)")

def feladat5(megoldas, valaszok):
    print("5. feladat:")
    sorszam = int(input("A feladat sorszáma: "))

    helyes_tippek = 0

    for szemely_adat in valaszok:
        if megoldas[sorszam-1] == szemely_adat[1][sorszam-1]:
            helyes_tippek += 1 

    szazalek = round((helyes_tippek / len(valaszok) * 100), 2)

    print(helyes_tippek, szazalek)



if __name__ == '__main__':

    valaszok, megoldas = feladat1()
    feladat2(valaszok)
    ell_valasz = feladat3(valaszok)
    feladat4(megoldas, ell_valasz)
    feladat5(megoldas, valaszok)
