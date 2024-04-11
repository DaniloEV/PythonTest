#
import pandas as pd
import sys as sys
import matplotlib.pyplot as plt
import seaborn as sns


#leer documento
df = pd.read_csv(f"{sys.path[0]}\\datosIngresos.csv")

#toma la info del source
sns.barplot(x="Tipo",y="Ingresos",data=df)

# plt.plot("01-09",12,"o")

totalIngresos = df["Ingresos"].sum()


#Muestra el total


#pinta la informacion
plt.show()