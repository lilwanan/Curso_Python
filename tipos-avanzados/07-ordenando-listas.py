numeros = [2, 4, 1, 45, 75, 22]
numeros.sort()
print(numeros)
numeros.sort(reverse=True)
print(numeros)
numeros2 = sorted(numeros)
print(numeros2)
numeros2 = sorted(numeros, reverse=True)
print(numeros2)
usuarios = [[4, "Chanchito"], [1, "Felipe"], [5, "Pulga"]]
usuarios.sort()
print(usuarios)
usuarios = [["Chanchito", 4], ["Felipe", 1], ["Pulga", 5]]


def ordena(elemento):
    return elemento[1]


usuarios.sort(key=lambda el: el[1])
print(usuarios)
