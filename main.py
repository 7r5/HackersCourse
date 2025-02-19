lista_de_años = [1998, 2017, 1999, 2011, 2003, 1997]

for año in lista_de_años:
    edad = 2025 - año
    print('La persona tiene (o cumplira este año)', edad, 'años')
    if edad > 18:
        print('la persona SI es mayor de edad:', año)
    else:
        print('la persona NO es mayor de edad:', año)
    print()