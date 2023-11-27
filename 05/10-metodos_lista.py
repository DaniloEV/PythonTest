#List crea una lista
lista = list(["aaa","aa"])
lista2=list()

lista2.append("Mi valor")

print(lista2)

#Len obtiene el tamaño de una lista
lenvalor=len(lista2)

print(lenvalor)

#APPEND Agrega un elemento a la lista, en la ultima posicion
lista2.append("Mi valor2")
print(lista2)

#Insert agrega un elemento a la lista en un indice que yo quiera
lista2.insert(1,"Mi valor3")
print(lista2)

#extend agrega varios elementos a la lista
listaAux=["aux","aux2"]
lista2.extend(listaAux)
print(lista2)

#Pop elimina un elemento de una lista, pide indice y devuelve el valor
lista2.pop(1)
print(lista2)
#Con -1 puedo eliminar desde atras, eliminando el último si es lo que deseo
#puede ser -1, -2 , etc...
lista2.pop(-1)
print("POP" + str(lista2))
#Remove remueve un elemento de una lista, pide el valor
lista2.remove("aux")
print("Limpiado Remove" + str(lista2))

#Clear limpia todo
lista2.clear()
print("Limpiado todo" + str(lista2))


#Sort ordena una lsita de forma ascendente a descendente
listaNumeral= list([5,4,1,True,0,-1,1.2,2.4]) #IMPORTANTE TRUE tendrá mayor valor que 2 y será menor a cualquier valor antes de 1.9999...
listaNumeral.sort()
print("Sort" + str(listaNumeral))

#Reverse invierte los elementos de una lista
listaNumeral.reverse()
print("reverse" + str(listaNumeral))

#Index busca el indice donde se encuentra un elemento en la lista
elemento=listaNumeral.index(True)
print("index " + str(elemento))