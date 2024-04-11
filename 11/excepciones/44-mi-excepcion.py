#Esto ya forma parte del curso de POO
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"La cagaste tu error es: {err}")
        
        

try:
    raise MiExcepcion("División cero")
except :
    print("que hiciste??")