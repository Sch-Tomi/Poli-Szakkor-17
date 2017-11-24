# Infók
A teszteléshez elengedhetetlen, hogy a tesztelőnek megfelelően alakítsuk ki a kódot. A tesztelő visszatérési értéket elemez ki vagyis nem kell semmit a képernyőre írni, de lehet.

A program fájl nevének *tesztverseny.py*-nek kell lennie

## Feladatok
A feladatoknak a következőképpen kell kinézniük.

- feladat2(valaszok)
- feladat3(valaszok)
- feladat4(keresett_valasz, megoldas)
- feladat5(megoldas, valaszok)
- feladat6(megoldas, valaszok)
- feladat7(ertekelesek)

Ahol a
- valaszok - a valasz.txt válaszai
- megoldas - a valasz.txt első sora
- keresett_valasz - egy szöveg, ami egy játékos válaszát mutatja
- ertekelese - pontszámok... amit a 6. feladat állít elő

### 2. feladat
*feladat2(valaszok)*

**Visszatérés:** egy szám

### 3. feladat
*feladat3(valaszok)*

**infó:** a versenyző azonsítóját az input()-tal kaphatjuk meg.

**Visszatérés:** egy szöveg, az adott versenyző válaszai

### 4. feladat
*feladat4(keresett_valasz, megoldas)*

**Visszatérés:** egy tömb, amiben "+" vagy " " szerpel attól függően h jól oldotta meg vagy sem


### 5. feladat
*feladat5(megoldas, valaszok)*

**infó:** a feldat sorszámát az input()-tal kaphatjuk meg.

**Visszatérés:** két visszatérési érték, az első hányan oldották meg jól, a második a százalékos arány

pl.:
```python
return (jol_oldottak_meg, szazalek)
```

### 6.feladat
*feladat6(megoldas, valaszok)*

**Visszatérés:** egy tömbök tömbje (mátrix), egy bejegyzés egy azonosítból és a pontszámból áll. Lásd minta.

**MINTA** 
```python
[["AB123", 3], ["DSA432", 22], ["OJK654", 777], ...]
```

### 7.feladat
*feladat7(ertekelesek)*

**Visszatérés:** egy tömbök tömbje (mátrix), egy bejegyzés egy helyezésből és egy azonosítóból áll.

**MINTA** 
```python
[[1, "AB123"], [2, "ASD123"], [2, "OJK654"], [3, "OOK333"]]
```

## Tesztelés
```bash
python teszt_tesztverseny.py
```