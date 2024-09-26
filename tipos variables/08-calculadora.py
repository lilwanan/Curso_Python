n1 = input("Ingresa primer numero: ")
n2 = input("Ingresa segundo numero: ")
n1 = int(n1)
n2 = int(n2)
print(n1, n2)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

mensaje = f"""
Para los numeros {n1} {n2}
El resultado de la suma es {suma}
El resultado de la resta es {resta}
El resultado de la multiplicacion es {multi}
El resultado de la divison es {div}
"""
print(mensaje)
