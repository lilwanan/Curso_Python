import json
from pathlib import Path

# productos = [{"id": 1, "name": "surfboard"},
#              {"id": 2, "name": "bicicleta"},
#              {"id": 3, "name": "skate"}]

# data = json.dumps(productos)
# print(data)
# Path("archivos/productos.json").write_text(data)

data = Path("archivos/productos.json").read_text(encoding="utf-8")
productos = json.loads(data)
# print(productos)
productos[0]["nombre"] = "Chanchito Feliz"
Path("archivos/productos.json").write_text(json.dumps(productos))
