#IMPORTANTE al ser un modulo debe tener un archivo __init__.py
#Representa que Python reconozca que es un paquete, en caso de no tenerlo no pasa nada, pero sirve para que enrute correctamente

from saludos import saludar as sl,saludar_avanzado as sl_a
import saludos.saludar

print(f"Con path puedo saber la ruta, porque el contiene el init {saludos.__path__}")
print(sl.Saludo("HOLA"))
print(sl_a.Saludo_completo("HOLA"))
