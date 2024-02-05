
import sys
print(sys.path)

#ABRO ARCHIVOS
archivo = open(f"{sys.path[0]}\\archivo.txt")

# #Leo archivos, no está en UTF-8
# print(archivo.read())
# print("=====================================================")
# print("=======================UTF-8=========================")
# print("=====================================================")
archivoUTF8 = open(f"{sys.path[0]}\\archivo.txt", encoding="UTF-8")

# #Leo archivos, está en UTF-8
# data_archivo=archivoUTF8.read()

# print(f"type {type(data_archivo)}   \n DATA {data_archivo}")

# print("=====================================================")
# print("=======================LINEAS========================")
# print("=====================================================")
# #Leo y separo el texto entre cada linea
# #En caso de que lo abra antes no lo puedo abrir y que lea linea por linea
# data_lineas=archivoUTF8.readlines()

# print(f"type {type(data_lineas)}   \n DATA {data_lineas}")


print("=====================================================")
print("================PRIMERA LINEA========================")
print("=====================================================")
#Leo y obtiene la primera linea de texto encontrada
#En parametros le puedo mandar la cantidad de letras que le quiero leer de la primera linea
data_linea=archivoUTF8.readline(5)

print(f"type {type(data_linea)}   \n DATA {data_linea}")

#cerrar archivo
archivoUTF8.close()