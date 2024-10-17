from time import ctime
from pathlib import Path

archivo = Path("archivos/archivo-prueba.txt")
# archivo.exist()
# archiv.rename()
# archivo.unlink()
# print(archivo.stat())

print("acceso", ctime(archivo.stat().st_atime))
print("creacion", ctime(archivo.stat().st_ctime))
print("modificacion", ctime(archivo.stat().st_mtime))
