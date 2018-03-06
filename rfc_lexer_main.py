
from rfc_lexer import *
from barra import*



if __name__ == '__main__':


    print("  ********************************************************************")
    print("  ***                        █  LEXER PYTHON                       ***")
    print("  ***                                                              ***")
    print("  ***          █ AUTORES: RICARDO PELAEZ Y FREDY RIVERA            ***")
    print("  ***          █ FECHA:   6/03/2018                                ***")
    print("  ***                                                              ***")
    print("  ***            UNIVERSIDAD DEL MAGDALENA - COMPILADORES          ***")  
    print("  ********************************************************************")
    print("\n\n")

    archivo = open("codigo.rfc", "r")  #abrimos el archivoW
    
    texto = []
    for linea in archivo:
    	texto.append(linea.strip())   #Guarda Linea por Linea en una lista
    archivo.close()

    for i in range(len(texto)):      # mandamos a evaluar cada linea de codigo , para ser evaluado con   nuesra regla del lenguaje
    	if texto[i] :
            esperar()                   #imprimimos la barra
            rfc_lexer(texto[i],i)       # evaluamos cada linea del codigo
    	 


    

