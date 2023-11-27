#Metodos diccionario
#IMPORTANTE DE PYTHON EL NONE ES LO MISMO QUE EL UNDEFINED O EL NULL
diccionario = {
    
    "General" : {
        "Nombre" : "OBJETO-A-1",
        "Valor" : "A-1",
        "Seccion" : "A",
        "Asiento" : "1"
    },
    "Grada" : {
        "Nombre" : "Grada-C-1",
        "Valor" : "C-1",
        "Seccion" : "C",
        "Asiento" : "1"
    }
}
#Keys() Devuelve las claves
keysDiccionario=diccionario["General"].keys()
print(keysDiccionario)

#get() devuelve el valor de una clave
getDiccionario=diccionario["General"].get("Nombre")
#El get en caso de no tener nada me tira un none, si lo coloco con las llaves provoca un exception
getDiccionarioNone=diccionario["General"].get("Nombre2")
print(getDiccionario)
print("getDiccionarioNone "+ str(getDiccionarioNone))

#clear() limpia todo
diccionario.clear()
print(diccionario)

#pop elimina un elemento
diccionario2 = {
    
    "General" : {
        "Nombre" : "OBJETO-A-1",
        "Valor" : "A-1",
        "Seccion" : "A",
        "Asiento" : "1"
    },
    "Grada" : {
        "Nombre" : "Grada-C-1",
        "Valor" : "C-1",
        "Seccion" : "C",
        "Asiento" : "1"
    },
    "Grada2" : {
        "Nombre" : "Grada-C-1",
        "Valor" : "C-1",
        "Seccion" : "C",
        "Asiento" : "1"
    }
}
diccionario2.pop("General")
print("POP" + str(diccionario2))


#items para iterar un diccionario
items_iterable=diccionario2.items()
print("items_iterable " + str(items_iterable))



