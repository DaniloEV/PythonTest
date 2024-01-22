diccionario = dict(nombre="lucas",apellido="juan", sueldo="1000")

#Obtener el valor del diccionario IMPORTANTE
for value, data in diccionario.items():
    print(f"Key ---{value}--- , data {data}")
    
    
#Obtener el key del diccionario IMPORTANTE
for value in diccionario.keys():
    print(f"Key {value}")
     
#Obtener el key del diccionario
for value in diccionario:
    print(f"Key {value}")