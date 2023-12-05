import math

#duraciones promedio
otros_cursos_min = 2.5
otros_cursos_max= 7
otros_cursos_promedio= 4
dalto_curso=1.5

#Diferencias de duración
diferencia_con_min = 100  - dalto_curso / otros_cursos_min * 100
print(f'La diferencia es de {diferencia_con_min}') 



diferencia_con_max = 100 - dalto_curso / otros_cursos_max * 100
print(f'La diferencia es de {math.floor(diferencia_con_max) } floor') 

#Lo que hace es que para obtener el valor según redondeo, corre la coma y lo divide
#según la cantidad de números que agregue debe ir subiendo la division para ir obteniendo más decimales
diferencia_con_max2 = 100 - dalto_curso * 1000 // otros_cursos_max / 10
print(f'La diferencia es de {diferencia_con_max2}') 

diferencia_con_promedio = 100 -  dalto_curso / otros_cursos_promedio * 100
print(f'La diferencia es de {diferencia_con_promedio}') 

crudo_promedio=5
crudo_dalto=3.5


#Punto B
tiempo_vacio_promedio = 100  - otros_cursos_promedio * 1000 // crudo_promedio / 10
print(f'Tiempo vacio de {tiempo_vacio_promedio}') 


tiempo_vacio_dalto = 100  - dalto_curso * 1000 // crudo_dalto / 10
print(f'Tiempo vacio de dalto {tiempo_vacio_dalto}') 



#Punto C ver 10 horas del curso
#De esta forma se encarga de redondear
#Oseaaa el ver este cursos me gano 27.3 de contenido
tiempo_horas_curso =  otros_cursos_promedio * 100 // dalto_curso / 10
print(f'Tiempo de 10 horas del curso de dalto equivale a ver de otros cursos {tiempo_horas_curso}') 



tiempo_horas_curso2 = dalto_curso  * 100 // otros_cursos_promedio / 10
print(f'Tiempo de 10 horas de ver otros cursos vs el de dalto es de {tiempo_horas_curso2}')  

