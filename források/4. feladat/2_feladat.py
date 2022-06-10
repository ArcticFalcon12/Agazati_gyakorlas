#2. feladat: Szökőévek
elso_evszam = int(input("Kérem az egyik évszámot:"))
masodik_evszam = int(input("Kérem a másik évszámot:"))
szokoevek = []
def szokoev(a: int, b: int):
    for i in range(a-1, b+1):
        if i % 400 == 0 or i % 4 == 0 and i % 100 != 0:
            szokoevek.append(i)
szokoev(elso_evszam, masodik_evszam)
print("Szökőévek:", str(szokoevek)[1:-1])