#encontrando el numero mayor de una lista
lista = [0,5,7,80,5,6]
numeroMasAlto=max(lista)
print(f"El número más alto es {numeroMasAlto}")

#Mas bajo
numeroMasBajo=min(lista)
print(f"El número más bajo es {numeroMasBajo}")

#bool IMPORTANTE
#retorna False si cumple con las siguientes condiciones
 #0, None, False
data = bool([0,5])
print(f"El valor de la validacion es {data}")


#retorna True si todos los valores son verdaderos deben serlos todos IMPORTANTE
#Dentro de la iteracion
allInfo = all([0,5])
print(f"El valor de la validacion all es {allInfo}")


suma = sum([0,5,7,80,5,6])
print(f"El valor de la validacion la suma es {suma}")