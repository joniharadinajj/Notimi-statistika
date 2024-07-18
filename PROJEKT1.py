'''
PROJEKTI NGA JONI HARADINAJ & EMA BYTYQI
'''

notat = {}
piket = int(input("Shkruaj numrin e nxënësve: "))
for i in range(piket):
    emri = input(f"Shkruaj EMRIN e nxënësit {i+1}: ")
    nota = float(input(f"Shkruaj PIKET e nxënësit {emri}: "))
    notat[emri] = nota

def lista():
    print("Lista e pikeve për nxënësit është:")
    for emri, nota in notat.items():
        print(f"{emri}: {nota}")
lista()

notat_lista = list(notat.values())

mesatarja = sum(notat_lista) / len(notat_lista)

minimale = min(notat_lista)

maximale = max(notat_lista)

print(f"Mesatarja e notave është: {mesatarja}")
print(f"Vlera minimale e notave është: {minimale}")
print(f"vlera maksimale e notave eshte: {maximale}")

def passed():
    for emri, nota in notat.items():
        if nota >= 60:
            print(f"{emri} passed")

def fail():
    for emri, nota in notat.items():
        if nota < 60:
            print(f"{emri} failed")

passed()
fail()



