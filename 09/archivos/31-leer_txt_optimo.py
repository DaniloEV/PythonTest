import sys
print(sys.path)


#! IMPORTANTE EL WITH FUNCIONA COMO UN USING
# SE EJECUTA LO DE DENTRO SOLO SI SE ABRIÓ CORRECTAMENTE
with open(f"{sys.path[0]}\\archivo.txt", encoding="UTF-8") as archivo:
    print("HOLA")
    print("MENOS RECURSOS,MÁS RAPIDO Y MEJOR")
    # print(archivo.read())
    print(archivo.readlines())