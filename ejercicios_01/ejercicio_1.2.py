promedio_tiempo_frase = 1
proedio_cantidad_palabras=2


dataUsuario=input("Decime una frase pa' : ")


cantidad_palabras_usuario=dataUsuario.split(" ")
tiempoPromedio=(len(cantidad_palabras_usuario) / promedio_tiempo_frase) * promedio_tiempo_frase 
print(f'Tiempo promedio es de {tiempoPromedio}')



if tiempoPromedio > 60 :
  print(f'Está reloco viejo hablás mucho')
  
  
  
  
tiempoPromedioDalto=len(cantidad_palabras_usuario) / promedio_tiempo_frase   * 1.3
print(f'Tiempo promedio es de {tiempoPromedioDalto}')