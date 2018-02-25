class Barra:
	iteracion=1
	total=1
	prefijo = ''
	sufijo = ''
	decimal = 1
	longitud = 100
	fill = 'ᛞ'
	def mostrar_Progreso_Barra (self):
   
    	porcentaje = ("{0:." + str(self.decimal) + "f}").format(100 * (self.iteracion / float(self.total)))
    	filledLength = int(self.longitud * self.iteracion // self.total)
    	bar = self.fill * filledLength + '-' * (self.longitud - filledLength)
    	
    	# Imprimir nuevo caracter 
    	if self.iteracion == self.total: 
        	print()
    return '\r%s โ%sโ %s%% %s' % (self.prefijo, bar, porcentaje, self.sufijo), end = '\r\r\r'	


caracteres = list(range(0, 50))
l = len(caracteres)       	

for i, caracteres in enumerate(caracteres):
	barra1=Barra()
	barra1.iteracion=i+1
	barra1.total=l
	barra1.prefijo='Progreso:'
	barra1.sufijo='Completado'
	barra1.longitud=50
	barra1.decimal=1
	fill = 'ᛞ'
	sleep(0.1)
	barra1.mostrar_Progreso_Barra()
    # Do stuff...
    
    