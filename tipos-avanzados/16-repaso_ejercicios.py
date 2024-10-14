string = "hola mundo este es mi string"


def quita_espacio(texto):
    return (char for char in texto if char != " ")


sinespacio = quita_espacio(string)
listatexto = list(sinespacio)
print(listatexto)

# 2


def cuentacaracter(lista):
    diccionario = {}
    for char in lista:
        if char in diccionario:
            diccionario[char] += 1
        else:
            diccionario[char] = 1
    return diccionario


diccionarionuevo = cuentacaracter(listatexto)
print(diccionarionuevo)


# 3

def ordenar(diccionario):
    return sorted(diccionario.items(), key=lambda key: key[1], reverse=True)


ordenados = ordenar(diccionarionuevo)
print(ordenados)


# 4

def mayores(lista):
    max_elemento = lista[0][1]
    diccionariomayores = {}
    for orden in lista:
        if max_elemento > orden[1]:
            break
        else:
            diccionariomayores[orden[0]] = orden[1]
    return diccionariomayores


mayoresss = mayores(ordenados)
print(mayoresss)
