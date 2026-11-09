users = ["Dave", "Jhon", "Sara"]

data = ["Dave", 2, True]

emptylist = []
# indicará que true, que si se encuentra
print("Dave" in data)

#False
print("Dave" in emptylist)


# con -1 o en negativo podemos obtener de atras hacía adelante
print(users[-1])
print(users[-2])
# index method para obtener el index
print(users.index("Sara"))

# por lista
# sin el ultimo
print(users[0:2])
# con posicion fija y hasta el final
print(users[1:])
# como el 0:2 pero en negativo
print(users[-3:-1])
# len para obtener los items
print(len(data))

# append
users.append("Elsa")
print(users)

# añadir a la lista una lista
users += ["Jason"]
print(users)

users.extend(["Robert", "Jim"])
print(users)

# por posición
users.insert(0,["Robert2", "Jim2"])

# se puede agregar datos por rangos sin perder los anteriores
# los mueve solo
users[2:2] = ["Robert3", "Jim3"]

#ahora reemplazando, 
# !NOTA ENTIENDO QUE ES MÁS POR EL RANGO,
# SI ES EL MISMO NO PASA NADA PERO SI ES NUMEROS DIFERENTES 
# ENTONCES SI REEMPLAZA
users[1:3] = ["RobertJPS", "JimJPS"]

print(users)
# remove
users.remove("RobertJPS")
print(users)

# pop sacar el ultimo, retorna el valor por si lo ocupamos
print(users.pop())

# borrar una posición
del users[0]

# en caso de borrar un objeto, con el del lo que hace es que 
# incluso en memoría deja de existir, si lo trato de 
# referenciar no existe
# del data

# clear para ello
data.clear()


# !Nota ordenarlo o reverse modifica el array a como estaba
# ordenar , si es string ordenará por capitalizadas y después 
# minusculas
users.sort()

# si quiero especificarle el tipo de ordenamiento y que
# con las mismas reglas de peso alfabetico
users.sort(key=str.lower)


nums = [4,42,74,1,5]
nums.reverse()
# nums.sort(reverse=True)
# print(nums)

# Con el sorted no modifica el array original, me 
# retona una copia
print(sorted(nums, reverse=True))
print(nums)

# tres maneras de copiar el array original
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

# tipado
print(type(nums))

mylist = list([1, "Neil", True])
print(mylist)



#########################################################
# Tuples, son más para no mutar, son más para leer que escribir
mytuple = tuple(('Dave', 42, True))
anothertuple = (1, 4, 2, 8, 2, 2)


print(mytuple)
print(type(mytuple))
print(type(anothertuple))

# se pueden convertir a lists
newlist = list(mytuple)
newlist.append('Neil')

# y volver al tuple con nuestra lista
newtuple = tuple(newlist)
print(newtuple)

# es como un desempaquetado
# one trae posición 0
# * me permite traer la lista de elemenos restantes
# hey en este caso trae la ultima posicion
(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))