condicion_1 = 3 > 2  # True
condicion_2 = 4 == 2 # False

if condicion_1:
    # si la condicion se cumple:
    pass
else:
    # si la condicion no se cumple:
    pass

# -------------------

if condicion_2:
    # si la condicion se cumple:
    pass
elif condicion_1:
    # si la condicion se cumple:
    pass
elif not condicion_1:
    # si la condicion se cumple:
    pass
else:
    # si la condicion no se cumple:
    pass

# -------------------
# Esto...
if condicion_2:
    print(condicion_1) # si la condicion se cumple:  # noqa: E701
else:
    pass

# es igual a:

if condicion_2: print(condicion_1) # si la condicion se cumple:  # noqa: E701
else:
    pass

# Ejercicio 1 ----------------------
# Imprime:
# si 'A' es mayor a 'B' - 'A es mayor a B'
    # si 'B' es menor que '50' - imprime 'A es mayor a 'B' y tambien es menor que 50'
    # si 'B' no es menor que '50' - imprime ' A es menor que B pero mayor que 50'
# Si 'A' es menor a 'B' - 'B es mayor a A'
# Si 'A' es igual a '33' - 'La variable A es igual a 33'
# Si 'B' el numero es diferente que '30' - 'B es diferente a 30'
# Si no se cumple nada de eso, imprime 'Else'

a = 10
b = 100

if condicion_1_0:
    # print mensa
    if condicion_1_1:
        pass
    elif condicion_1_2
        pass
elif condicion_2_0
?

# Ejercicio ---------------------- Validar que un numero no esta dentro del rango
# crea 2 condiciones
a = 65
# condicion_a: a es menor que 100
# condicion_b: a es mayor que 0
# crea una condicion donde se imprima 'Error: El numero debe estar entre 0 y 100'
# solo imprimir si las 2 condiciones no se cumplen (si al menos una esta mal)



# ejemplos NOT (invierte el valor booleano True/False)
if not True and (not False):
    print('Pepito')
else:
    print('Cacahuate')

a = 33
b = 200

# Esto ...
if a:
  print("a is NOT greater than b")
# Es igual a esto porque python toma el valor entero 0 como False, todo lo demas es True
if a != 0:
    print("a is NOT greater than b")
# -----
if '': # Un string vacio tambien regresa el oeprador logico False si lo usamos en condiciones
  print("a is NOT greater than b")

if a != '':
    print("a is NOT greater than b")
    