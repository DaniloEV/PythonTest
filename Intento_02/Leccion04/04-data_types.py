import math

# literal assignment
first = "Dan"
last = "Espinoza"

# imprime str
print(type(first))
# imprime true
print(type(first) == str)
# imprime true
# el segundo puede ser int, float, etc
print(isinstance(first, str))

# constructor function
# funciona de igual manera como un string
pizza = str("Peperoni")


# Concatenacion
fullName = first + " " + last
fullName += "!"
fullName2 = f"${first} - ${last}"

# Casting a number to a string
# de int a string
decade = str(1980)
print(decade)


#permite el salto de linea, para multiples lineas
multilinea = """string multi
    de una nueva linea con salto"""
mismoMultilinea = '''salto
    de linea'''

# Escapint special characters
# \' me permite hacer un escape character cuando se tiene un string con ''
# \t es tab, \n salto linea
sentance = 'I\'m back at work!\t Hey! \n\n Here'

#String methods
#lower retorna no cambia la variable
print(first.lower())
#upper igual 
print(first.upper())
#capitalize
firstLetter = first.capitalize()
print(firstLetter)
# title coloca la primer letra capitalizada del string
print(multilinea.title())
#replace 
print(multilinea.replace("salto","intento de salto"))
#len cuenta caracteres
print(len(multilinea))

#strip para quitar espacios
multilinea = multilinea.strip()

# Build a menu
title = "menu".upper()
#Centra el titulo y agrega = hasta que tenga 20 de longitud
print(title.center(20,"="))
#Agrega . hasta cumplir con 16 de longitud
print("Coffee".ljust(16,".") + "$1".rjust(4))
print("Coffee 2".ljust(16,".") + "$2".rjust(4))
print("Coffee 3".ljust(16,".") + "$3".rjust(4))
print("Coffee 4".ljust(16,".") + "$4".rjust(4))


# string index value (string como array)
# que igual inicia en 0 los arrays
print(title[1])
# con -1 indica la ultima posicion
print(title[-1])
# por rangos, con el range no es que provee la ultima 
print(title[0:-1])
# por rangos, ahora si porque no le indico hasta donde
print(title[0:])

# Metodos que retornan bool
#startswith("D")
#endswith("D")

# int(valor) castea 
# bool(valor) castea 
# float(valor) castea 

# complex type
# más que todo para electrical engineering que usan 
# j-notation
comp_value = 5+3j
print(comp_value.real)
print(comp_value.imag)


# Built-in functions for numbers
gpa = 3.28
print(abs(gpa))
# el absoluto será en positivo siempre
print(abs(gpa * -1))

print(round(gpa))
# aunque el round es redondeo hacía el entero más cercano
# el segundo parametro lo convierte a float, siendo o busca
# el decimal más cercano
# solo round = 3 , con segundo parametro 3.3
print(round(gpa, 1))


# import math
print(math.pi)
print(math.sqrt(64))
#techo
print(math.ceil(gpa))
#suelo
print(math.floor(gpa))


