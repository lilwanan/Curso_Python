# METODO JUANI

# print("""
# Bienvenidos a la calculadora
# Para salir escribe Salir
# Las operaciones son suma, multi, div y resta

# """)
# numero1 = input("Ingresa un numero: ")
# numero1 = int(numero1)
# operacion = input("Ingresa operacion: ")
# numero2 = input("Ingresa siguiente numero: ")
# numero2 = int(numero2)
# suma = numero1 + numero2
# resta = numero1 - numero2
# multi = numero1 * numero2
# div = numero1 / numero2

# while operacion.lower != "salir":
#     if operacion == "suma":
#         print(f"El resultado es: {suma}")
#     elif operacion == "resta":
#         print(f"El resultado es: {resta}")
#     elif operacion == "multi":
#         print(f"El resultado es: {multi}")
#     else:
#         print(f"El resultado es: {div}")
#     operacion = input("Ingresa operacion: ")
#     if operacion == "salir":
#         break


# METODO LIBRO

print("Bienvenidos a la calculadora")
print("Para salir escribe salir")
print("Las operaciones son suma, resta, multi y div")

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese numero: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
        op = input("Ingresa operacion: ")
        if op.lower() == "salir":
            break
        n2 = input("Ingresa siguiente numero: ")
        if n2.lower() == "salir":
            break
        n2 = int(n2)
        if op.lower() == "suma":
            resultado += n2
        elif op.lower() == "resta":
            resultado -= n2
        elif op.lower() == "multi":
            resultado *= n2
        elif op.lower() == "div":
            resultado /= n2
        else:
            print("Operacion no valida")
            break

        print(f"El resultado es: {resultado}")
