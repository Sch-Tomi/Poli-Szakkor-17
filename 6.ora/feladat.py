
fajl = open("adat.txt", "r")

sorok = fajl.readlines()
adat = []

for sor in sorok:
    adat.append(sor.replace("\n", "").split(";"))

print(adat)

fajl.close()