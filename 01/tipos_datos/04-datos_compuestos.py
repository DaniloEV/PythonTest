#datos agrupados 

#lista, modicable 
lista = ["Juanito", 'Youtube', 1000, True]

print(lista[0])

#tuplas, iguales a la lista, en vez de corchetes [], utiliza ()
#la tupla no se puede modificar
lista2 = ("Juanito2", 'Youtube', 1000, True)
# lista2[0]="aa"
print(lista2[0])

#conjunto set --> set (conjunto)
#no soportan indexación y no se puede modificar un valor del conjunto
#no permite datos duplicados
#no tiene datos en misma posición
conjunto = {"Lucas","soy",True,1.85}
conjunto.add("addd")
print(conjunto)

#diccionario
diccionario = {
    'Pedro' :  {
        'persona':"Pedro",
        'altura':1.86
    },
    'Juan':{
        'persona':"Juan",
        'altura':1.85
    }
}
print(diccionario["Pedro"]['altura'] + 2)