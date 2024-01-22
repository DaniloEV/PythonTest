frutas = ["bamnama","manzana","manzana2","manzana3","manzana4","manzana5"]

#For con continue
for var in frutas:
    if var =="manzana":
        #El continue se salta el elemento de esa iteración incluyendo el print aunque no esté dentro del if
        #Resumen salta el valor de esa iteracion
        continue
    print(f"Me he comido una {var}")
    
#For con break
#El break se salta todo y cierra incluyen el else del for, lo ignora
for var in frutas:
    if var =="manzana":
        break
    print(f"Me he comido una {var}")
else :
    print("He terminado :)")
    
#Cadenas de texto
#Puede ser solo el valor ya que lo reconoce como tal o puede ser con el enumerate
miNombre="Hola Soy Nadir"
for valor in miNombre:
    print(valor)
    
#Ciclo en una sola linea de código
numeros = [0,1,2,4,8]

numerosDuplicados = [x*2 for x in numeros]
print(numerosDuplicados)