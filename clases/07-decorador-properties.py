class Perro:
    def __init__(self, nombre):
        self.set_nombre = (nombre)

    @property
    def get_nombre(self):
        print("pasando por getter")
        return self.__nombre

    @get_nombre.setter
    def set_nombre(self, nombre):
        print("pasando por setter")
        if nombre.strip():
            self.__nombre = nombre
        return nombre


perro = Perro("Choclo")
print(perro.get_nombre)
