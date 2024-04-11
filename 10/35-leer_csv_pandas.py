import pandas as pd
import sys 

print(type(pd))
#dataframe = df
# obtener la info del dataframe normal
df = pd.read_csv(f"{sys.path[0]}\\datos.csv")
print(df)

# se puede obtener con columna
print(df["nombre"])

#obtener la info del dataframe normal, le puedo poner nombres a las columnas sería para casos en que la primera columna es un valor
# df = pd.read_csv(f"{sys.path[0]}\\datos.csv", names=["name","lastname","age"])
# print(df)
# #se puede obtener con columna
# print(df["name"])


#ordenar el dataframe por edad
df_ordenadoAsc=df.sort_values("edad")
print(df_ordenadoAsc)

#descendente
df_ordenadoDes=df.sort_values("edad",ascending=False)
print(df_ordenadoDes)

#concatenando dos frame
df2 = pd.read_csv(f"{sys.path[0]}\\datos.csv")

df_contenado = pd.concat([df2,df])
print(f"contanenado {df_contenado}")

#accediendo a la primeras filas con head(), es tipo first o el número que le indique
#si le pongo 1 me muestra el primero, si le pongo 3 me trae los 3 primeros
primeras_filas = df_contenado.head(3)
print(f"primeras_filas {primeras_filas}")


#accediendo a las ultimas filas con tail(), es tipo first o el número que le indique
#si le pongo 1 me muestra el primero, si le pongo 3 me trae los 3 primeros
ultimas_filas = df_contenado.tail(1)
print(f"ultimas_filas {ultimas_filas}")


#accediendo a cantidad filas y columnas con shape, primero filas, despues columnas
contadorFilas_Columnas = df_contenado.shape
print(contadorFilas_Columnas)


#desempaquetado
filas,columnas= df_contenado.shape
print(f"Filas {filas}")
print(f"Columnas {columnas}")

#obteniendo datos estadisticos
df_info = df_ordenadoAsc.describe()
print(df_info)

df_info2 = df.describe()
print(df_info2)

#acceder a datos segun fila o columna por loc o iloc el slicing me permite obtener todo el rango de datos
nombre = df.loc[:,"nombre"]
print(nombre)

apellidosILoc = df.loc[:,"apellido"]
print(apellidosILoc)



fila3 = df.loc[2,:]
print(f"fila3 {fila3}")

#permite validaciones igual
mayor_30 = df.loc[df["edad"] >30 ,:]
print(f"mayor_30 {mayor_30}")

