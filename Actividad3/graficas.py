from os import remove
import pandas as pd
import seaborn
import matplotlib.pyplot as plt 
import numpy as np
import seaborn as sns



file = './data.csv'

df = pd.read_csv(file)



#energy ,tempo
#Acceder a valores

print( "valores unicos de energy: ",df["energy"].unique()) 
columna = df["energy"]        
print("Promedio: ",columna.mean())       
print("Mediana: ",columna.median())      
print("Maximo:",columna.max())        
print("Minimo:",columna.min())         
print("Desviación estandar:",columna.std()) 

df.hist(column="energy", grid=False, orientation="vertical", color = "coral")
plt.show()

df.boxplot(column=["energy"], color = "green", showmeans=True )
plt.show()

#remove outliers
df2 = df[df["energy"]>=.2]

df2.boxplot(column=["energy"], color = "green", showmeans=True )
plt.show()

print( "valores unicos de tempo: ",df["tempo"].unique()) 
columna = df["tempo"]  
print("Promedio: ",columna.mean())       
print("Mediana: ",columna.median())      
print("Maximo:",columna.max())        
print("Minimo:",columna.min())         
print("Desviación estandar:",columna.std())  

df.hist(column="tempo", grid=False, orientation="vertical", color = "blue")
plt.show()

df.boxplot(column=["tempo"], color = "red", showmeans=True )
plt.show()


plt.figure(figsize=(15, 5))
sns.heatmap(df.corr(), annot=True, vmin=0, vmax=1, cmap="cividis");
plt.show()

