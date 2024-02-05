import sys
print(sys.path)

# no significa que agrega el archivo, sino que al final va y agrega la linea
#! IMPORTANTE EL WITH FUNCIONA COMO UN USING
# SE EJECUTA LO DE DENTRO SOLO SI SE ABRIÓ CORRECTAMENTE
with open(f"{sys.path[0]}\\archivo2.txt",'a', encoding="UTF-8") as archivo:
    #Sobre escribe el archivo y le cae encima
    # archivo.write("HEYYYY")
    #Escribe de linea en linea, permite enviarle un array para controlar y mandar
    archivo.write("\n")
    archivo.writelines(["HEYY \n","HEYY \n","HEYY \n"])
    archivo.writelines(["AQUIII EL RICH!!"])
    archivo.write("\n")
    
    for i in range(5):
        archivo.write(f"Escribo linea {i+1} \n")
    #DOS WRITELINES JUNTOS LO ENTIENDE COMO SI FUERA PARA EL MISMO ARCHIVO, TRABAJA EN CONJUNTO HASTA QUE CIERRE, IDEAL PARA ARRAYS