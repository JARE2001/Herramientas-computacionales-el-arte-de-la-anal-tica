##############################################################
#Ruta del archivo
##############################################################

file = './data.csv'
import pandas as pd

df = pd.read_csv(file)
shape = df.shape
print("numero de registros", shape[0])
print("numero de variables", shape[1])
columns = df.columns
print("columnas: ")
for el in columns:
    print(el)
print("columnas y tipo: ")
print(df.dtypes) 



#quita los renglones (axis=0) que contienen cualquier (how='any', 'all') columna vacía, inplace significa que modifica el dataframe df
df.dropna(axis = 0, how = 'any', inplace = True)


#energy ,tempo
#Acceder a valores 
print( "valores unicos de energy: ",df["energy"].unique()) 
columna = df["energy"]        
print("Promedio: ",columna.mean())       
print("Mediana: ",columna.median())      
print("Maximo:",columna.max())        
print("Minimo:",columna.min())         
print("Desviación estandar:",columna.std()) 

print( "valores unicos de tempo: ",df["tempo"].unique()) 
columna = df["tempo"]  
print("Promedio: ",columna.mean())       
print("Mediana: ",columna.median())      
print("Maximo:",columna.max())        
print("Minimo:",columna.min())         
print("Desviación estandar:",columna.std())  
