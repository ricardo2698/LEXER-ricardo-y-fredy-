
import lexer

RESERVADO = 'RESERVADO'
ENTERO   = 'N_ENTERO'
VARIABLE = 'VARIABLE'
#FLOTANTE = 'FLOTANTE'
BOOLEANO ='BOOL'
#todas las espresiones de entero, reservadas y identificadoras
token_exprsiones = [
    (r'[ \n\t]+',              None),
    (r'@[^\n]*',               None),
    (r'\<-',                   RESERVADO),
    (r'\(',                    RESERVADO),
    (r'\)',                    RESERVADO),
    (r':',                     RESERVADO),
    (r'\+',                    RESERVADO),
    (r'-',                     RESERVADO),
    (r'\*',                    RESERVADO),
    (r'/',                     RESERVADO),
    (r'menor_igual',           RESERVADO),
    (r'menor',                 RESERVADO),
    (r'mayor_igual',           RESERVADO),
    (r'mayor',                 RESERVADO),
    (r'diferente',             RESERVADO),
    (r'igual',                 RESERVADO),
    (r'Y',                     RESERVADO),
    (r'O',                     RESERVADO),
    (r'negacion',              RESERVADO),
    (r'si',                    RESERVADO),
    (r'entonces',              RESERVADO),
    (r'si_no',                 RESERVADO),
    (r'mientras_que',          RESERVADO),
    (r'constante',             RESERVADO),
    (r'hacer',                 RESERVADO),
    (r'para',                  RESERVADO), 
    (r'fin',                   RESERVADO),
    (r'VERDADERO',             BOOLEANO),
    (r'FALSO',                 BOOLEANO), 
    (r'[0-9]+' ,                ENTERO),
    #(r'[+-]?\d+(\.\d+|[eE][+-]?\d+)?',     FLOTANTE),
    (r'[A-Za-z][A-Za-z0-9_]*', VARIABLE),
    
]

def rfc_lexer(texto,i):
    return lexer.lexer(texto, token_exprsiones,i)
