import sys, csv
print(sys.path)


#Leer archivo csv
with open(f"{sys.path[0]}\\datos.csv", encoding="UTF-8") as archivo:
    print("Hola lo tengo")
    # print(archivo.readlines())
    #el reader lo interpreta como un datatable
    readerData= csv.reader(archivo)
    for row in readerData:
        print(row)
        for col in row:
            print(col)
    
    # print(csv.reader(archivo))