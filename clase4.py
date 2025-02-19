import pprint

nombres = ['Ricardo', 'elvia']
diccionario = {'edad': 23, 'asdfasdf': 'ASDFasdf2f2ef'}
lista_de_diccionarios = [{'edad': 23}, {'edad': 23}, {'edad': 23}]
edades = [26, 27]
edades.append(99)
print('Las edades son', edades)
edad = [True, False, True]

var_diccionario = {'nombre': 'Ricardo', 'edad': 26}
lista_de_diccionarios = [
    {'nombre': 'Ricardo', 'edad': 26, 'hobbies': ['Impresion 3d', 'Monas chinas', 'Drones']},
    {'nombre': 'Elvia', 'edad': 28, 'hobbies': ['Series', 'Comer' ,'Hechar weba'] },
    {'nombre': 'Yane', 'edad': 10, 'hobbies': ['Estudiar', 'Bailar' ] },
    ]
lista_de_diccionarios.append( {'nombre': 'Luis', 'edad': 1, 'hobbies': ['trocas' ,'gta V', 'Comprar Tenis'] })
#informacion_luis = lista_de_diccionarios[3]
#lista_de_hobbies_de_luis = informacion_luis['hobbies']
#for hobbie in lista_de_hobbies_de_luis:
#    print('-', hobbie)

#pprint.pp(lista_de_diccionarios)
print('-------------------------')
print('-------------------------')
print('-------------------------')
print('-------------------------')
print('-------------------------')

for persona in lista_de_diccionarios:
    print(persona.get('nombre'))
    for hobbie in persona.get('hobbies'):
        print('-', hobbie)
    print()

print('-------------------------')
# Esto es lo mismo a ...
for persona in lista_de_diccionarios:
    if persona.get('edad') > 18:
        persona.update({'es_mayor': True})
    else:
        persona.update({'es_mayor': False})

# Estooooooo ->
for persona in lista_de_diccionarios:
    if persona.get('edad') > 18:
        resultado_texto = 'Si'
    else:
        resultado_texto = 'No'
    persona.update({'es_mayor_de_edad': resultado_texto})

pprint.pp(lista_de_diccionarios)
print('-------------------------')
