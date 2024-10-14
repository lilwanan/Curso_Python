# 1
def quita_espacios(texto):
    return [char for char in texto if char != " "]


string = "hola mundo este es mi string"
sin_espacios = quita_espacios(string)
lista_string = list(sin_espacios)

print(lista_string)

# 2


def cuentaletras(lista):
    diccionario_char = {}
    for char in lista:
        if char in diccionario_char:
            diccionario_char[char] += 1
        else:
            diccionario_char[char] = 1
    return diccionario_char


diccionario_contado = cuentaletras(lista_string)
print(diccionario_contado)


# 3


def ordena(diccionario):
    return sorted(diccionario.items(),
                  key=lambda key: key[1], reverse=True)


ordenado = ordena(diccionario_contado)
print(ordenado)


# 4

def mayores(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        else:
            respuesta[orden[0]] = orden[1]
    return respuesta


mayor = mayores(ordenado)
print(mayor)

# 5


def crea_mensaje(diccionario):
    mensaje = "los que mas se repiten son: "
    for key, valor in diccionario.items():
        mensaje += f"{key} con {valor} repeticiones "
    return mensaje


mensaje2 = crea_mensaje(mayor)
print(mensaje2)
