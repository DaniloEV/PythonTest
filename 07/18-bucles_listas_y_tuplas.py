#Todo esto funciona para listas y tuplas y conjuntos (set)
#Repetir de forma controlada un elemento
listaAnimales = ["gato","perro","cerdo","loro"]


for item in listaAnimales:
    print(f'Animal: {item}')
    
variable = dir(listaAnimales)
print(variable)


numeros=[5,7,9,13,15,16]

#Funciona como el for each
for num in numeros:
    valor=num*num
    print(valor)
    num=valor
    print(num)

#No modifica dentro de la misma lista si lo quiero reasignar
print(f"numeros modificados {numeros}")

#ZIP para iterar dos o más listas al mismo tiempo, llegará hasta donde ambas listas su siguiente valor no sea None (null)
# Para eso debería idealmente ser del mismo tamaño
for numero,animal in zip(numeros,listaAnimales):
        print(f'ZIP: {numero}')
        print(f'ZIP: {animal}')
        
        
#region For normal con indice

#Iterar por range
#Si quiero darle un inicio lo puedo hacer, caso contrario que inicie de cero con solo un parametro
#Funciona como el for normal
#No es la forma más optima 
#IMPORTANTE!!! NO FUNCIONA PARA CONJUNTOS
# for num in range(len(numeros)):
#     print(f'range index: {num} ----')
#     print(f'range value: {numeros[num]}')
    
#La mejor manera es con enumerate
for i,val in enumerate(numeros):
    print(f'enumerate: {val}') 
    print(f'Index Enumerate {i} ---- Value {val}')
#endregion   


#for else
#Me indica que cuando finaliza el bucle puedo realizar una accion
for i, val in enumerate(numeros):
    print(f'Index Enumerate {i} ---- Value {val}')
else:
    print("Bucle terminado")
