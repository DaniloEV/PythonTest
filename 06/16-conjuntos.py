conjunto = set(["dato1", "dato2"])


conjunto.add("dato3")
print(conjunto)


##Para poder agregar un conjunto dentro de otro conjunto no se puede agregar normal
#Sino que se ocupa un set de tipo frozenset

conjuntoFrozen= frozenset(["dato4","dato5"])

conjuntoTotal = {conjuntoFrozen,"dan"}
print(dir(conjuntoTotal))

#Teoria de conjuntos
conjunto1={1,3,5,7,9}
conjunto2={1,3,7}


#saber si un conjunto es subconjunto de otro
resultado=conjunto2.issubset(conjunto1)
print(resultado)

resultado2=conjunto1.issubset(conjunto2)
print(resultado2)

#O se puede hacer
resultado3 =conjunto2  <=conjunto1
print(resultado3)

#Saber si es un superconjunto (Tiene más info)
resultado2=conjunto1.issuperset(conjunto2)
print(resultado2)

#O se puede hacer
resultado3 =  conjunto1 >= conjunto2
print(resultado3)



#verificar si hay data igual 
resultado4 =  conjunto1.isdisjoint(conjunto2)
print(resultado4)