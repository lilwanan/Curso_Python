from pathlib import Path
path = Path("rutas")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename()
for p in path.iterdir():
    print(p)

archivos = [p for p in path.iterdir() if not p.is_dir()]
print(archivos)

archivos = [p for p in path.glob("01-*py")]
print(archivos)
archivos = [p for p in path.glob("**/*py")]
print(archivos)
archivos = [p for p in path.rglob("*.py")]
print(archivos)
