buscar = 3
for numero in range(5):
    # logica
    # muestra un numero de veces igual a numero el mensaje de hola mundo
    # print(numero, numero * "hola mundo")
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print("No encontre el numero buscado :(")

for char in "Ultimate python":
    print(char)
