from os import remove
import pandas as pd
import seaborn
import matplotlib.pyplot as plt 
import numpy as np
import seaborn as sns
from sklearn.cluster import KMeans


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

#kmeans -------------------

test = df[["tempo","energy"]]
test = test.dropna(axis = 0, how = 'any')

kmeans = KMeans(n_clusters=3).fit(test)
centroids = kmeans.cluster_centers_
print(centroids)

# Predicciones (cuál es la clase) de acuerdo a los centros calculados

cla = kmeans.predict(test)                   # obtiene las clases de los datos iniciales

# # Predicción para un nuevo dato
# data = {'km': ['100'], 'vehicle_year': [2002]}
# newdf = pd.DataFrame(data)  
# print(kmeans.predict(newdf))


plt.scatter(df["tempo"],df["energy"],c=cla)
for i in range(len(centroids)):
    plt.scatter(centroids[i][0],centroids[i][1],marker="*",c="red")

plt.show()


test = df[["acousticness","energy"]]
test = test.dropna(axis = 0, how = 'any')

kmeans = KMeans(n_clusters=3).fit(test)
centroids = kmeans.cluster_centers_
print(centroids)

# Predicciones (cuál es la clase) de acuerdo a los centros calculados

cla = kmeans.predict(test)                   # obtiene las clases de los datos iniciales

# # Predicción para un nuevo dato
# data = {'km': ['100'], 'vehicle_year': [2002]}
# newdf = pd.DataFrame(data)  
# print(kmeans.predict(newdf))


plt.scatter(df["acousticness"],df["energy"],c=cla)
for i in range(len(centroids)):
    plt.scatter(centroids[i][0],centroids[i][1],marker="*",c="red")

plt.show()