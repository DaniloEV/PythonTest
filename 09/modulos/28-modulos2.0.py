# Importante , con la carpeta permite organizar mejor y más segmentado, igual para acomodar
# Si estuviera dentro de una carpeta en la misma ruta
import modulos_nuevos.modulo_saludo as saludo


print(saludo.Saludo("Juan"))


# Importante sys
import sys
print(f"Me dice que es {sys} ")
print(f"TODOS LOS MODULOS DE PYTHON INTEGRADOS {sys.builtin_module_names}")

# Adicional si ocupo puedo agregar nuevas ya que es un arreglo
print(f"Me da las rutas que tengo de base en sys y donde corre mi app {sys.path}")