import pprint

lista_de_productos = [
    {"Nombre": "Coca Cola", "Id": 1001, "Precio_bruto": 45.2, "Cantidad": 10},
    {"Nombre": "Submarinos", "Id": 1002, "Precio_bruto": 30.8, "Cantidad": 6},
    {"Nombre": "Doritos", "Id": 1003, "Precio_bruto": 21.4, "Cantidad": 0},
    {"Nombre": "Yakult", "Id": 1004, "Precio_bruto": 7.0, "Cantidad": 45},
]

pprint.pp(lista_de_productos)

for producto in lista_de_productos:
    producto.update()

# imprimir todo el diccionario con pprint

# Cada Dictionario de producto debe tener un nuevo campo que se va
# a llamar 'Precio_publico' y que sea el precio bruto mas el 15%
