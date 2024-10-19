# from io import open

# texto = "Hola mundo"

# archivo = open("archivos/hola-mundo.txt", "w")
# archivo.write(texto)
# archivo.close()

# archivo = open("archivos/hola-mundo.txt", "r")
# texto = archivo.read()
# archivo.close()
# print(texto)

# archivo = open("archivos/hola-mundo.txt", "r")
# texto = archivo.readlines()
# archivo.close()
# print(texto)
# with open("archivos/hola-mundo.txt", "r") as archivo:
#     print(archivo.readlines())
#     archivo.seek(0)
#     for linea in archivo:
#         print(linea)

# archivo = open("archivos/hola-mundo.txt", "a+")
# archivo.write("Chao mundo")
# archivo.close()

with open("archivos/hola-mundo.txt", "r+") as archivo:
    texto = archivo.readlines()
    archivo.seek(0)
    texto[0] = "Chanchito feliz"
    archivo.writelines(texto)
