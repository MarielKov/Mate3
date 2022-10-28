import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import StandardScaler

import seaborn as seabornInstance 
import sklearn.model_selection 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


df = pd.read_csv('D:/Unsam/Mate3/Unsam.Clase.11/Unsam.Clase.11/cvs_para_el_TP/runners.csv')
print(df)
print("--------------------------------- \n")
print(df.shape)
print("--------------------------------- \n")
print(df.describe())
print("--------------------------------- \n")
X = df.iloc[:, :-1].values
print(X)
print("--------------------------------- \n")
y = df.iloc[:, 5].values
print(y)
print("--------------------------------- \n")

if (df.isnull().values.any() == True):

    print(df.isnull().any())
    df.isnull().sum().sum()
    nan_rows = df[df.isnull().any(1)]
    print("--------------------------------- \n")
    print(nan_rows)
    imputer = SimpleImputer(missing_values = np.nan, strategy="mean")
    print("--------------------------------- \n")
    print(X[:,6:8])
    imputer = imputer.fit(X[:,6:8])
    X[:,6:8] = imputer.transform(X[:,6:8])
    print("--------------------------------- \n")
    print(X[:,6:8])
    print("--------------------------------- \n")


print(X)
print("--------------------------------- \n")

labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
X[:, 4] = labelencoder_X.fit_transform(X[:, 4])
X[:, 5] = labelencoder_X.fit_transform(X[:, 5])

print(X)
print("--------------------------------- \n")

onehotencoder = make_column_transformer((OneHotEncoder(), [3]), remainder = "passthrough")
X = onehotencoder.fit_transform(X)
print(X)

print("--------------------------------- \n")
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)
print(y)
print("--------------------------------- \n")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


print(X_train)
print(X_test)
print(y_train)
print(y_test)
print("--------------------------------- \n")

sc_X = StandardScaler()

X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

print(X_train)
print("--------------------------------- \n")
print(X_test)
print("--------------------------------- \n")

print("max peso: ",df['pulso.antes'].max())
print("min peso: ",df['pulso.antes'].min())
print("max pulso.despues: ",df['pulso.despues'].max())
print("min pulso.despues: ",df['pulso.despues'].min())

X = df['pulso.despues'].values.reshape(-1,1)
y = df['pulso.antes'].values.reshape(-1,1)
df_aux = pd.DataFrame({'X': X.flatten(), 'y': y.flatten()})
print("--------------------------------- \n")
print(df_aux)

regression = LinearRegression()
regression.fit(X_train, y_train)
#y_prediction_lr = regression.predict(X_test)
#y_prediction_lr = np.round(y_prediction_lr)

print("--------------------------------- \n")
print(regression.intercept_)
print("--------------------------------- \n")
print(regression.coef_)
print("--------------------------------- \n")

y_pred = regression.predict(X_test)

df_aux = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})

print(df_aux)


plt.plot(X_test, y_pred, color='red', linewidth=2)
df.plot(x='pulso.despues', y='peso', style='o')
plt.title('Pulsasiones despues de correr y Peso')
plt.ylabel('Peso')
plt.xlabel('Pulsasiones despues de correr')
plt.show()



seabornInstance.displot(df["pulso.despues"])
plt.title('Pulsasiones despues de correr y Peso')
plt.ylabel('Peso')
plt.xlabel('Pulsasiones despues de correr')
plt.show()




#plt.figure(figsize=(15,10))
#plt.tight_layout()
df1 = df_aux.head(91)
df1.plot(kind='bar',figsize=(16,10))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()



plt.scatter(X_test, y_test)
#plt.plot(X_test, y_pred, color='red', linewidth=70)

plt.title('Pulsasiones despues de correr y Peso')
plt.ylabel('Peso')
plt.xlabel('Pulsasiones despues de correr')
plt.show()




print('Error Absoluto Medio:',metrics.mean_absolute_error(y_test, y_pred)) 
print("--------------------------------- \n")
print('Error Cuadratico Medio:', metrics.mean_squared_error(y_test, y_pred)) 
print("--------------------------------- \n")
print('Raíz del error cuadrático medio:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))












