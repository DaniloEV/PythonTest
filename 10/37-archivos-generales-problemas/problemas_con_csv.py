import pandas as pd
import sys

#cargar dataframe
df = pd.read_csv(f"{sys.path[0]}\\datos.csv")

print(df)

#cambiar el tipo de dato de una columna, para manejarlo a mi manera, no es que lo cambie en el excel
df['edad'] = df['edad'].astype(str)
print(type(df['edad'][0]))

#reemplazar valores dentro del excel
df['apellido'].replace('Dalto','maestro',True)
print(df)

#eliminar datos de una fila vacia, tiene sobrecarga para columnas o filas
# df= df.dropna()

#eliminar filas repetidas
# df= df.drop_duplicates()

#crear nuevo archivo de tipo xlsx
df.to_csv(f"{sys.path[0]}\\datos_nuevos.csv")