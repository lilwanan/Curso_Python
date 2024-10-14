class Usuario():
    def guardar(self):
        print("guardando en la BBDD")


class Sesion():
    def guardar(self):
        print("Guardando en archivo")


def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()


usuario = Usuario()

sesion = Sesion()

guardar([sesion, usuario])
