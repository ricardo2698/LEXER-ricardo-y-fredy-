from time import sleep

def mostrar_Progreso_Barra (iteracion, total, prefijo = '', sufijo = '', decimal = 1, longitud = 100, fill = '█'):
   
    porcentaje = ("{0:." + str(decimal) + "f}").format(100 * (iteracion / float(total)))
    filledLength = int(longitud * iteracion // total)
    bar = fill * filledLength + '-' * (longitud - filledLength)
    print('\r%s .%s.  %s%% %s' % (prefijo, bar, porcentaje, sufijo), end = '\r\r\r')
    # Imprimir nuevo caracter 


    if iteracion == total: 
        print()

       

"""
caracteres = list(range(0, 50))
l = len(caracteres)

#  muestra desde  0%

for i, caracteres in enumerate(caracteres):
    # Do stuff...
    sleep(0.1)
    # Actualizando el proseco de barra
    mostrar_Progreso_Barra(i + 1, l, prefijo = 'Progreso:', sufijo = 'Completado', longitud = 50)
"""
def esperar():
    caracteres = list(range(0, 50))
    l = len(caracteres)

    #  muestra desde  0%

    for i, caracteres in enumerate(caracteres):
        # Do stuff...
        sleep(0.02)
        # Actualizando el proseco de barra
        mostrar_Progreso_Barra(i + 1, l, prefijo = 'Progreso:', sufijo = 'Completado', longitud = 50)
