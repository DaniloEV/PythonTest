#lamba son como las de JS o bueno parecidas... 
# en este caso son anonimas no tienen nombre
# retorna solo
multiplicar_por_valor = lambda x,y: x*y

print(multiplicar_por_valor(2,5))


#usando filter con una funcion comun
#filter se encarga de validar una funcion y ejecutar esa funcion en medida de la lista que yo le pase
#en resumen filtra la lista según la funcion que le pase y me da los valores según el return le indique
numeros = [1,2,3,4,5,6,7,8,9,11,13,14,15,20]
#se puede pasar una funcion lambda como paretro
numeros_pares = filter(lambda numero:numero % 2==0,numeros)
#el como tal no es la lista debo pasarlo
print(numeros_pares)
# es tipo filter
print(type(numeros_pares))
# se convierte a lo que ocupe
print(tuple(numeros_pares))