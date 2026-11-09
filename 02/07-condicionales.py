#condicionales
edad = 18
edad_minima=18
if edad >= edad_minima:
    print("Pasar")
    print("Pasar2")
    #Accion que se ejecuta
else :
     #accion de else
    print("No pasar")
    print("No pasar2")
    print("No pasar3")

print("De fijo pasa sin importar condicion")





#elif

# Se utiliza and, not or
# Para validar 
ingreso=1500

if ingreso < 100 :
  print("Sos pobre")
elif ingreso >= 1000 and ingreso <= 5000: 
  print("Sos medio estado")
else:
  print("Sos Goz")
  
valor = not ingreso 

valor2Opcional = ingreso > 100 or ingreso < 500 

#Ternario
print("Right") if valor2Opcional else print("Not")