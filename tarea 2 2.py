
dias_de_la_semana = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
letra_inicial = 'j'
for dia in dias_de_la_semana:
    if dia.startswith(letra_inicial):
        print('El dia', dia, 'SI empieza con', letra_inicial)
    else:
        print('El dia', dia, 'NO empieza con', letra_inicial)
    
