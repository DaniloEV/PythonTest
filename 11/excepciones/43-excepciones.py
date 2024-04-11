def dividir():
    a = input("Valor 1: ")
    b = input("Valor 2: ")
    resultado = 0
    try: 
        aConvertido = int(a)
        bConvertido = int(b)
        # if bConvertido == 0:
        #       raise Exception("El dividendo no puede ser cero, guacho")
        resultado = aConvertido / bConvertido
    except: 
        print(f"Te caiste maestro, hiciste algo mal") 
    else:
        print("Todo bien guacho!") 
        return resultado


def dividir2():
    a = input("Valor 1: ")
    b = input("Valor 2: ")
    resultado = 0
    try: 
        aConvertido = int(a)
        bConvertido = int(b)
        if bConvertido == 0:
            raise Exception("El dividendo no puede ser cero, guacho")
        resultado = aConvertido / bConvertido
    except Exception as e: 
        print(f"Te caiste maestro, hiciste algo mal Error --> {e}") 
    else:
        print("Todo bien guacho!") 
        return resultado
    finally:
         print("Finalizando...") 
    
print(dividir2())

#Try anidados
# try:
#   f = open("demofile.txt")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")