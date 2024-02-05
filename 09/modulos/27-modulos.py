# Esto es un namespace, contenedor
# As es como asignar un nuevo nombre y distinguirlo  si lo hago así debo de llamarlo completo
import modulo_saludo as m_sal

# m_sal.saludo("Nombre")


# Tambien si solo ocupo una cosa de un modulo, ya sea un clase, un metodo o lo que sea que haya definido lo puedo llamar con from 
# tambien se puede cambiar el nombre
from modulo_saludo import Saludo, Saludo_completo
# se trae todo
# from modulo_saludo import *


#IMPORTANTE!!! Se comporta como un método por aparte
saludoSimple = Saludo("Danilo")
print(saludoSimple)


saludoComplejo = Saludo_completo("Danilo")
print(saludoComplejo)


#ver propeirdades y metodos
print(dir(m_sal))