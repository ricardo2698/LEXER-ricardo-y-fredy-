
RESERVADO = 'RESERVADO'
ENTERO      = 'N_ENTERO'
VARIABLE       = 'VAR'
flotante = 'flotante'
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
    (r'Menor_igual',           RESERVADO),
    (r'Menor',                 RESERVADO),
    (r'Mayor_igual',           RESERVADO),
    (r'mayor',                 RESERVADO),
    (r'Diferente',             RESERVADO),
    (r'Igual',                 RESERVADO),
    (r'Y',                     RESERVADO),
    (r'O',                     RESERVADO),
    (r'Negacion',              RESERVADO),
    (r'Si',                    RESERVADO),
    (r'entonces',              RESERVADO),
    (r'Si_No',                 RESERVADO),
    (r'Mientras_Que',          RESERVADO),
    (r'Constante',             RESERVADO),
    (r'Hacer',                 RESERVADO),
    (r'Para',                  RESERVADO), 
    (r'Fin',                   RESERVADO),
    (r'[0-9]+',                N_ENTERO),
    (r'[A-Za-z][A-Za-z0-9_]*', VAR),
]

