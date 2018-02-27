
# Arena

Célunk egy aréna játék készítése, amiben hősök küzdenek egymással. Egy hőst különboző eszközökkel szerehetünk fel. Ezek befolyásolják, a képességeit.

## Items
Kezdjük el a tárgyak létrehozását.
### 1.1 Item

 - Hozzuk létre a projekt mappánkban a `item.py` fájlt.
 - Hozzuk létre a `Item` osztályt.
 - Az `Item` osztálynak a következő változói vannak:
	 - bonusStr 
     - bonusAgi 
     - bonusInt 
     - armor 
     - hpRegen 
     - bonusDmg 
 - Ezeket inicializáskor 0-ra álltítjuk.
 - Hozzunk létre minden változónak egy get függvényt.
		Vagyis `get_bonusStr`, `get_bonusAgi`, ezek adják vissza az adott értéket.
 - Hozzunk létre, az add_ előtagos függvényeket is amikkel hozzá adhatunk értéket minden változóhoz. **Hozzáadni nem simán `=`(!!!)**
 - Hozzunk létre, egy info függvényt, ez írjon ki minden adatot. [Lustáknak...](#help1)
 - Örülünk kész az alap Item osztály! :)
 
 ### 1.2 Konkrét Tárgyak
 - Hozzuk létre az `items.py` fájlt.
	Ebben fogjuk elhelyezni a tárgyakat. 
	Az alap tárgyaknál be kell állítani a bónuszokat. Amiket más tárgyakból rakunk össze ott örökölni fogjuk.
#### Chain Mail 
![enter image description here](https://cdn.steamstatic.com/apps/dota2/images/items/chainmail_lg.png)
 Közepes szövésű láncing. 
 ##### Recept:
 - alap tárgy 
 ##### Tulajdonságai:
 - +5 páncél 


----------


 #### Plate Mail 
![enter image description here](https://cdn.steamstatic.com/apps/dota2/images/items/platemail_lg.png?3)
Vastag fémvértezet, ami megvédi a teljes felsőtestet.
 ##### Recept:
 - alap tárgy 
##### Tulajdonságai:
 - +5 páncél 

----------
 #### Assault Cuirass
![enter image description here](https://cdn.steamstatic.com/apps/dota2/images/items/assault_lg.png?3)
Ez az Alsóbb Régiók mélységeiben kovácsolt pokoli lemezpáncél megnövelt páncéllal. 
##### Recept:
 - Plate Mail
 - Chain Mail
##### Tulajdonságai:
 - Örököltek!
##### Segítség:
Létrehozás:
```python
class AssaultCuirass(ChainMail, PlateMail):
```
Örökölni meg így kell:
```python
super().__init__()
```
##### Teszt
Honnan tudod, hogy sikerült örökölni a tulajdonságokat?
```python
a = AssaultCuirass()
print(a.info()) 
```
Azt írja +15 páncél

----------
 #### Broad Sword
![enter image description here](https://cdn.steamstatic.com/apps/dota2/images/items/broadsword_lg.png?3)
A lovagok klasszikus választása, ez a penge robusztus és megbízhatóan öli az ellenségeket. 
##### Recept:
 - alap
##### Tulajdonságai:
 - +18 sebzés 

----------
 #### Robe Of The Magi
![enter image description here](https://cdn.steamstatic.com/apps/dota2/images/items/robe_lg.png?3)
Ez a köpeny megrontja viselője lelkét, de cserébe bölcsességet ad. 
##### Recept:
 - alap
##### Tulajdonságai:
 - +6 intelligencia 

 #### Blade Mail
![enter image description here](https://cdn.steamstatic.com/apps/dota2/images/items/blade_mail_lg.png?3)
Egy pengeéles lemezpáncél, az önzetlen mártírok választása a harcban. 
##### Recept:
 - Chain Mail
 - Robe of the Magi
##### Tulajdonságai:
 - Örökölt!
----------
 #### Blades of Attack
![enter image description here](https://cdn.steamstatic.com/apps/dota2/images/items/blades_of_attack_lg.png?3)
Eme apró elrejthető pengék sebzése nem lebecsülendő. 
##### Recept:
 - alap
##### Tulajdonságai:
 - +9 sebzés 

----------
 #### Crystalys
![enter image description here](https://cdn.steamstatic.com/apps/dota2/images/items/lesser_crit_lg.png?3)
Egy ritka kristályokból kovácsolt penge, mely az ellenség páncéljának gyenge pontjait keresi. 
##### Recept:
 - Blades of Attack
 - Broad Sword
##### Tulajdonságai:
 - Örökölt

----------
 #### RING OF REGEN
![enter image description here](https://cdn.steamstatic.com/apps/dota2/images/items/ring_of_regen_lg.png?3)
Ez a gyűrű a gnómok körében szerencsét hozó kabalának számít. 
##### Recept:
 - alap
##### Tulajdonságai:
 - +1.5 életerő-töltődés

----------
 #### RING OF HEALTH
![enter image description here](https://cdn.steamstatic.com/apps/dota2/images/items/ring_of_health_lg.png?3)
Egy csillogó gyűrű, melyet egy dagadt félszerzet holtteste alatt találtak. 
##### Recept:
 - alap
##### Tulajdonságai:
 -  +5 életerő-töltődés 

----------
 #### Cloak
![enter image description here](https://cdn.steamstatic.com/apps/dota2/images/items/cloak_lg.png?33)
Egy mágikus anyagból készült köpeny.
##### Recept:
 - alap
##### Tulajdonságai:
 -  +2 páncél

----------
 #### HOOD OF DEFIANCE
![enter image description here](https://cdn.steamstatic.com/apps/dota2/images/items/hood_of_defiance_lg.png?3)
Egy prémes, mágiával szemben ellenálló fejfedő, melyet félnek a varázslók. 
##### Recept:
 - Cloak
 - Ring of Health
 - Ring of Regen
##### Tulajdonságai:
 -  Örökölt!

## Hero
Kezdjük el megírni a hős osztályunkat.

### Init
- Hozzuk létre a `hero.py` fájlt amiben a hősünket írjuk majd.
- Hozzuk létre a `Hero` osztályt ebben.
- Az inicializáskor 5 dolgot kell megadnunk, a hősünkkel kapcsolatban:
	- Név (name)
	- Erő (strength)
	- Ügyesség (agility)
	- Inteligencia (inteligence)
	- Alapsebzés (damage)
- Ezeket a kapott paramétereket mentsük el pl: `__baseStrength`
- Ezeken kívül szükségünk van még a tényleges képességek tárolására, vagyis az előző listára, de már csak pl `__strength` ebbe már beleszámolódik az a képesség ami tárgyaktól jön. Ezek legyenek inicializálás során  kezdeti értékek.
- Továbbá szükségünk van még a következő változókra (Ezek lehetnek nullák alapból):
	- Életerő (hp)
	- Max életerő (maxHP)
	- Gyógyulás (hpRegen)
	- Pajzs (Armor)
- Készítsük el a Hősünk inventory-ját is, ami egy egyszerű lista lesz.
### Inventory
- Készitsük el az `addItem()` függvényt aminek egyetlen paramétere egy `item`
	- Ez a függvény nem csinál mást mint hozzá adja az itemet az invetory-hoz
	- Oldjuk meg hogy csak 6 tárgyat birtokolhassunk, ha már van 6 tárgyunk akkor nem kell hozzáadni és nem is kell figyelmeztetni.
### Stats
- Most hogy tudunk tárgyakat birtokolni frissítenünk kell tudni a tárgyak alapján, a képességeinket.
	- Hozzuk létre a `__recalcStats` függvényt.
	- Számoljuk ki az erőnket, ehhez az sima erő változatunkat kell módosítanunk képlet hozzá:
		- `erő = alapErő + itemBonus`
		- Az `itemBonus` kiszámolásához hozzunk létre egy függvényt `__calcBonusStrength` néven.
			- Ez a függvény adjon vissza egy számot. 
			- Valamint menjen végig az összes itemen, és kérje le a `get_bonusStr()` függvény segítségével a plussz erőt
	- Most hasonló módon számoljuk ki a ügyeség, az inteligencia és a sebzés pontunkat is.
	- Most már többi dolgunkat is:
		- `maxHp = 20 * erő`
		-	`hpRegen = 0.03 * erő` 
		-	`armor = 0.14 * ügyesség + bonusArmor` (a bonus armort ugyan úgy kell megkapnunk mint az `itemBonust`)
-	Ezek után tegyük meg, hogy hívjuk meg a `__recalcStats` fg-t amikor új itemet kapunk, illetve az inicializálás végén.
-	Hozzuk létre a `__regenToMaxHp` fg-t is. Ez állítsa be az életerőnket, a maximumra.

## Helps
### Help1
```python
def info(self):
        return "+Strength: {}\n+Agility: {}\n+Inteligence: {}\n+Damage: {}\n+Armor: {}\n+HP Regen: {}".format(
            self.bonusStr, self.bonusAgi, self.bonusInt, self.bonusDmg, self.armor, self.hpRegen)
```