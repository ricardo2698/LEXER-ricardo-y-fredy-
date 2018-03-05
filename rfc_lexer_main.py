
from rfc_lexer import *
from barra import*
from time import sleep


if __name__ == '__main__':
    archivo = open("codigo.rfc", "r")
    #esperar()      # se llama ala funcion que muestra la barras de espera

    texto = []
    for linea in archivo:
    	texto.append(linea.strip())   #Guarda Linea por Linea en una lista
    archivo.close()

    for i in range(len(texto)):      # mandamos a evaluar cada linea de codigo , para ser evaluado con   nuesra regla del lenguaje
    	esperar()
    	#tokens = rfc_lexer(texto[i],i) 


    



