"""f = open("lexerr.rfc", 'w') 
f.write('hola mundo cruell')
f.close()

archivo = open("lexerr.rfc", "r") 
linea1 = archivo.readline()
print (linea1)
contenido = archivo.read()
print contenido

archivo = open("lexerr.rfc", "r") 
for linea in archivo.readlines():
    print linea
    """

archivo = open("lexerr.rfc", "r+")
contenido = archivo.read()
final_de_archivo = archivo.tell()
lista = ['Línea 1\n', 'Línea 2']
 
archivo.writelines(lista)
archivo.seek(final_de_archivo)
 
print archivo.readline()
# Línea 1
 
print archivo.readline()
# Línea 2    