# Infók
A teszteléshez elengedhetetlen, hogy a tesztelőnek megfelelően alakítsuk ki a kódot. A tesztelő visszatérési értéket elemez ki vagyis nem kell semmit a képernyőre írni, de lehet.

A program fájl nevének *hiányzások.py*-nek kell lennie

## Feladatok
A feladatoknak a következőképpen kell kinézniük.

- feladat3(naplo)
- feladat5()
- feladat6(naplo)
- feladat7(naplo)

Ahol a
- naplo - a naplo.txt feldolgozott változata

### 1-2. feladat
Vegyük észre, hogy a második feladatra sokkal egyszerűbb válaszolni ha az első feladatban megszámoljuk a sorokat. Ezért a második feladat így térjen vissza:
pl.:
```python
return (naplo, bejegyzesek)
```

Ahol a bejegyzesek egy szám.

### 3. feladat
*feladat3(naplo)*

**Visszatérés:** az igazolt és igazolatlan órák száma (a sorrend fontos! 1. igazolt, 2. igazolatlan)
Pl.:
```python
return (igazolt, igazolatlan)
```

### 4-5. feladat
Az ötödik feladat a 4. egy meghívása ezért a hetnapja fügvényt teszteljük.

*hetnapja(honap, nap)*

**Visszatérés:** egy nap, ékezet nélkül


### 6. feladat
*feladat6(naplo)*

**infó:** a napot és az órát input()-tal kérjük be. (Fontos a sorrend! 1. nap, 2. óra)

**Visszatérés:** hiányzások száma

### 7.feladat
*feladat6(megoldas, valaszok)*

**Visszatérés:** egy tömb, amiben a legtöbbet hiányzok neve van

**MINTA** 
```python
["Kiss Pista", "Gép Elek"]
```

## Tesztelés
```bash
python hianyzasok_test.py
```