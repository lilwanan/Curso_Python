class Caminador:
    def caminar(self):
        print("caminando")


class Volador:
    def volar(self):
        print("volando")


class Nadador:
    def nadar(self):
        print("nadando")


class Perro(Caminador, Nadador):
    def programar(self):
        print("programando")


class PezVolador(Volador, Nadador):
    def programar(self):
        print("programando")


class Pato(Volador, Nadador, Caminador):
    def programar(self):
        print("programando")
