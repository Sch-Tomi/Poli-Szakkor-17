from random import randint

#Ezeket találgathatom
szotar = ["almafa", "proramozás", "asztal", "pendrive"]

#Választunk egy random szót a szótárból, a random indexet a randint szolgáltatja 0 és szotar hossza - 1 között hogy ne legyen túl indexelve.
kitalalando = szotar[randint(0, len(szotar)-1)]

#Az aktuális állapotot tároljuk le
allas = ["_"]*len(kitalalando) # Python Hack "_" teli tömböt hoz létre annyi elemből ahány betű van a szóban

#Élet...
elet = 5

#Amiket már tippeltem
tippek = [""]

#Info üzenet
info = ""

#Játék fő ciklusa, amíg van életünk és van kitalálandó karakter
while elet > 0 and "_" in allas:
  
    #Felület kiírása
    print(*allas, end="\n\n") # *lista - lista elemket szét bontja és elválasztja alapértelmezetten
    print("Élet: " + str(elet), end="\n\n")  # end paraméter azt mondja meg hogy a kiírás végén milyen karakter legyen \n sortörés(újsor) \n\n dupla sor
    print("Tippek:", *tippek)
    print(info)
  
    tipp = input("Tipped: ").lower() # bekérünk egy tippet
  
    #Vizsgáljuk a tippeket
    if tipp in kitalalando and tipp not in tippek: # Ha még nem tippeltem és jó a tipp
    
        #Lecseréljük az összes karaktert amit jól tippelt
        for i in range(0, len(kitalalando)):
            if kitalalando[i] == tipp:
                allas[i] = tipp

        #Hozzá adjuk hogy ezt már tippelte
        tippek.append(tipp)
            
    elif tipp in tippek: #Ha már tippelte ezt, hiba üzi
        info = "Ezt már tippelted!"
    
    elif tipp not in kitalalando: #Ha hibásat tippeltem, hiba üzi
        info = "Ez a betű nincs benne."

        elet -= 1 # Szintaktikus cukorka jelentése elet = elet - 1 vagyis vonjunk ki eggyet a változóból
        tippek.append(tipp)



#Ciklus vége, játék vége
#2 lehetséges eset

if elet > 0: #Van élete tehát kitalálta
    print("Gratulálok kitaláltad! :)")
else: #Vagy nincs élete és nem találta ki
    print("Sajnállak akasztófa virág :(")

