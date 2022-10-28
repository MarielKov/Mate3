import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.impute import SimpleImputer
import seaborn as seabornInstance 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics



df = pd.read_csv('D:/Unsam/Mate3/Unsam.Clase.11/Unsam.Clase.11/cvs_para_el_TP/runners.csv', low_memory=False)
print(df.head())

print("--------------------------------- \n")

print(df.shape)

print("--------------------------------- \n")

print(df.describe())

print("--------------------------------- \n")

#Se eliminan las columnas innecesarias para este analisis
df.drop(df.columns[[0,3,4,5,6,7,8]],axis = 1,inplace = True)

print(df.head())

print("--------------------------------- \n")

#En caso de un valor faltantes, entra al if, si no, sigue con normalidad
if (df.isnull().values.any()):
    print(df.isnull().any()) #Impreme las columnas, donde haya un valor faltante saldra True
    print("--------------------------------- \n")
    print(df.isnull().sum().sum()) #Numero de valores faltantes 
    nan_rows = df[df.isnull().any(1)]
    print("--------------------------------- \n")
    print(nan_rows) #Se imprimen las filas donde estan los valores faltantes
    imputer = SimpleImputer(missing_values = np.nan, strategy="mean") 
    print("--------------------------------- \n")
    print(df)
    imputer = imputer.fit(df) #Se hace un promedio de todos los valores y se rellenan los NaN
    df = imputer.transform(df)
    print("--------------------------------- \n")
    print(df)
    print("--------------------------------- \n")
    #Tuve que hacerlo de esta forma porque el transform devuelve un array con flotantes y
    #tenia problemas para hacer los maximos y minimos, esta forma fue la unica que encontre para 
    #que no me diera un error
    df = pd.DataFrame(df.astype(int) ,columns=['pulso.antes','pulso.despues'])
    print(df)
# Fin if
    
#Maximos y minimos de cada columna
print("Maximos\n\n",df.max())

print("--------------------------------- \n")

print("Minimos\n\n",df.min())

print("--------------------------------- \n")

#print("Promedio\n\n",df.mean())


df.plot(x='pulso.antes', y='pulso.despues', style='o') 
plt.title('pulso.antes vs pulso.despues') 
plt.xlabel('pulso.antes') 
plt.ylabel('pulso.despues') 
plt.show()



seabornInstance.displot(df['pulso.despues'])
plt.show()

X = df['pulso.antes'].values.reshape(-1,1)
y = df['pulso.despues'].values.reshape(-1,1)
df_aux = pd.DataFrame({'X': X.flatten(), 'y': y.flatten()})

print(df_aux)

print("--------------------------------- \n")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
df_aux = pd.DataFrame({'X_train': X_train.flatten(), 'y_train': y_train.flatten()})

print(df_aux.head())

print("--------------------------------- \n")

df_aux = pd.DataFrame({'X_test': X_test.flatten(), 'y_test': y_test.flatten()})

print(df_aux.head())

print("--------------------------------- \n")

regressor = LinearRegression() 
regressor.fit(X_train, y_train) 

print(regressor.intercept_)

print("--------------------------------- \n")

print(regressor.coef_)

y_pred = regressor.predict(X_test)

print("--------------------------------- \n")

df_aux = pd.DataFrame({'Actual': y_test.flatten(), 'Prediccion': y_pred.flatten()})

print(df_aux)

print("--------------------------------- \n")

df1 = df_aux.head(25)
df1.plot(kind='bar')
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()

plt.scatter(X_test, y_test,  color='gray')
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.show()

print('Error Absoluto Medio:',metrics.mean_absolute_error(y_test, y_pred)) 

print("--------------------------------- \n")

print('Error Cuadratico Medio:', metrics.mean_squared_error(y_test, y_pred))

print("--------------------------------- \n")

print('Raíz del error cuadrático medio:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

print("--------------------------------- \n")
