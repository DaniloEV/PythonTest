#Los parametros args son parametros que de manera indefinida yo le puedo pasar para que no tengan limite
def suma(*numeros) : 
    return  sum(numeros)


resultado = suma(1,2,2,3,4,5)
print(resultado)
 
# los parametros args deben estar al final ya que si coloco otros estos se perderan
def suma(nombre ,*numeros) : 
    return f"Hola {nombre} la suma de tus valores es {sum(numeros)}" 


resultado2 = suma("Juan",1,2,2,3,4,5)
print(resultado2)
 