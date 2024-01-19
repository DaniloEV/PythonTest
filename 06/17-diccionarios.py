#diccionarios
# 
diccionario = dict(nombre="lucas",apellido="juan")
print(diccionario)

#una tupla o un frozenset puede ser una clave de un diccionario
#una lista, debido a que es iterable o un set, por tema de hash no lo pueden serlo
diccionario2= {("valor1","valor2"):"juan"}
print(diccionario2)

# fromkeys va a ser siempre el primer parametro el iterable, el segundo el valor por defecto
#Creando diccionario con dict.fromKeys(), crea los valores en NONE
diccionarioKeys=  dict.fromkeys(["Nombre"," Apellido"],"N/A")
print(diccionarioKeys)

#Por defecto si no le pongo un valor va a ser None
diccionarioKeys=  dict.fromkeys(["Nombre"," Apellido"])
print(diccionarioKeys)

#Debe mandar una lista porque si lo hago con un solo valor tomará que es un elemento de cada de un string
#Recordar al final que un string es una lista de char
diccionarioKeys=  dict.fromkeys("Nombre")
print(diccionarioKeys)