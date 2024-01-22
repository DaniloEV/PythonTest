#creando funcion simple 
def saludar(nombre, genero = ""):
    genero = genero.upper()
    if genero == "M":
        adjetivo = "maestra"
    elif (genero == "H"):
        adjetivo = "capo"
    else:
        adjetivo  = "crack" 
    
    
    print(f" Hola {nombre} mi {adjetivo} como andás?")



# dataUsuario=input("¿Cuál es tu nombre man?")
# saludar(dataUsuario) 

saludar("Juanito", "m") 
saludar("Juanito", "H") 



#crear funcion retornable

def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    print(f"Valor {num}")
    c1 = num - 2
    print(c1)
    c2 = num
    c3= num - 5
    print(c3)
    contraseña = f"{chars[c1]} {chars[c2]} {chars[c3]}"
    return contraseña

password = crear_contraseña_random(10)
print(f"Tu contraseña es {password}")


#crear funcion multiple valores retornables
# se le puede pasar una tupla, tecnicamente sigue siendo solo uno xD
# IMPORTANTE Python permite la sobre escritura del metodo 
def crear_contraseña_random(num,valor):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    print(f"Valor {num}")
    c1 = num - 2
    print(c1)
    c2 = num
    c3= num - 5
    print(c3)
    contraseña = f"{chars[c1]} {chars[c2]} {chars[c3]}"
    return (contraseña,num)

password2,valorNumero = crear_contraseña_random(10,0)
print(f"Tu contraseña es {password2}")
print(f"Tu contraseña es {valorNumero}")