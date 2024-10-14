class Perro:
    patas = 3

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice: Guau")


mi_perro = Perro("Chanchito", 1)
mi_perro.patas = 5
mi_perro2 = Perro("Felipe", 1)
# mi_perro.habla()
print(Perro.patas)
print(mi_perro.patas)
print(mi_perro2.patas)
