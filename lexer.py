from subprocess import check_output
import sys
import re

def lexer(texto, token_exprsiones,i):
    #print len(characters)
    
    
    pos = 0
    tokens = []
    while pos < len(texto):
        # print "que paso"
        match = None
        #print "cicloooooooo while" 
        for token_expr in token_exprsiones:
               
            patron, etiqueta = token_expr
            regex = re.compile(patron)
            match = regex.match(texto, pos)
            if match:
                text = match.group(0)
                if etiqueta:
                    #print "que paso"
                    token = (text, etiqueta)
                    tokens.append(token)
                    
                break
        if not match:            # si no esta en el patron de tokens  muestra el error

            ilegal=texto
            sys.stderr.write('Eroor!!! Illegal character (%s)\n' % ilegal[pos])
            print (" -> ' en la linea  ->",i+1 )
            linea=str(i+1)
            speak=check_output(['espeak','error  linea'])
            speak1=check_output(['espeak',linea])


            
            sys.exit(1)
        else:
            pos = match.end(0)
        #print pos
    if tokens:
        print (tokens ,"Token en la Linea ",i+1," Correto ¶")  

    return tokens
    