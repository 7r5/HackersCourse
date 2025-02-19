lista_de_años = [1998, 2017]

for año in lista_de_años:
    edad = 2025 - año
    print('La persona tiene (o cumplira este año)', edad, 'años')
    es_mayor_de_edad = edad >= 18
    print('variable booleana', es_mayor_de_edad)
    if False:
        print('la persona SI es mayor de edad:', año)
    else:
        print('la persona NO es mayor de edad:', año)
    print('-----')