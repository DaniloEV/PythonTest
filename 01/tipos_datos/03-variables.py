a=2
b=3
c= a + b #5

c+=c #10
c -=c #0
#str para mostrar las string
print("Cantidad " +  str(c))

#Contenar
name="Juan"
print("Hola Usuario " +  name)
#f strings
nombre='Mario'
bienvenida=f'Hola {nombre} ¿Cómo andas?'
print(bienvenida)

#del para borrar datos, si lo borro antes de aplicarlo en otra variable este si va a existir aún
del bienvenida
#print(bienvenida) 

#operadores de pertenencia (in and not in)
validar="Hola Amigo"
datoEncontrado="hola" in validar
print(datoEncontrado) 

datoNoEncontrado="hola" not in validar
print(datoNoEncontrado)

# e identidad