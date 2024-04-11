# dos listas nombre y apellidos y cargar en txt
nombres = ["JUAN","PEDRO","PEDRO2","JUAN2","JUAN3"]
apellidos = ["Dalto","Rodriguez","Rodriguez2","Rodriguez3","Rodriguez4"]

#registrar info en un txt de forma optima

with open("archivo_ejemplo.txt","w") as archivo: 
    archivo.writelines("Los Datos Son:\n")
    #for en una linea y escribir al mismo tiempo, es como si tuviera un for y corriera
    [archivo.writelines(f"---- Nombre: {n}\n ---- Apellido {a}\n ---------- \n ") for n,a in zip(nombres,apellidos)]