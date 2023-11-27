# metodos de las cadenas

cadena="Hola soy Juanito"
cadena2="Hola soy Juanito Para Prueba"

#Dir es una función que permite saber los metodos que tiene un tipo de variable, string, int, lista,etc
# print(dir("Hola Soy Cadena"))
# print(dir(4))
# print(dir([]))
###################################################

#Upper es un metodo de string/cadena
matus = cadena.upper()
print(matus)

#Lower es un metodo de string/cadena
minus = cadena.lower()
print(minus)

#Primer letra mayuscula
firstLetter = cadena.capitalize()
print(firstLetter)


#Find buscar una cadena en otra cadena, 
#Permite buscar por valor char o una cadena entera
#Me retorna la primer resultado (index) que encuentre
#-1 si no encuentra
search_find = cadena.find("a")
search_find2 = cadena.find("Prueba")
search_find3 = cadena.find("Juanito")

print(search_find)
print(search_find2)
print(search_find3)


#Index buscar una cadena en otra cadena, 
#Permite buscar por valor char o una cadena entera
#Me retorna la primer resultado (index) que encuentre
search_find4 = cadena.index("a")
#En caso de no encontrar me retorna una excepcion para controlar
#search_find5 = cadena.index("Prueba")
search_find6 = cadena.index("Juanito")

print(search_find4)
# print(search_find5)
print(search_find6)


#isNumeric  comprueba si lo que tiene la cadena es de tipo numerico
#OJO --> que sea numerico no que contenga numeros
cadena_numeric="22"
is_numeric=cadena_numeric.isnumeric()
print(is_numeric)

#isalpha
#OJO SOLO SI APLICA TRUE SI ESTÁ ENTRE A-Z LOS VALORES DE LA CADENA
cadena_alpha="Hola"
is_alpha=cadena_alpha.isalpha()
print(is_alpha)

#count, devuelve la cantidad de coincidencias que encuentre
count_coincidences="Holaaa"
count=count_coincidences.count("d")
print(count)


#len, cantidad de caracteres que tiene una cadena
lenData=len(count_coincidences)
print(lenData)

#endswith finaliza con dicha cadena
cadenaWith="Buenas buenas"
valueWith=cadenaWith.endswith("s")
print(valueWith)

#startswith
valueWith=cadenaWith.startswith("s")
print(valueWith)

#replace, no modifica el original
valueWith=cadenaWith.replace("a","e")
cadenaWith=valueWith
print(valueWith)
print(cadenaWith)

#split separa cadenas, con lo que le pase
data=cadenaWith.split(" ")
print(data)
print(cadenaWith)