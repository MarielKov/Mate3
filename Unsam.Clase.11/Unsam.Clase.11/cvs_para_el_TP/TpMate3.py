from sklearn.impute import SimpleImputer
import numpy as np
import pandas as pd
from sklearn.preprocessing import *
from sklearn.compose import make_column_transformer
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


df = pd.read_csv('video_juegos_populares.csv')
print(df)

x = df.isnull().any()
print(x)
print("+++++++++++")
df.isnull().sum().sum()
nan_rows = df[df.isnull().any(1)]
print(nan_rows)

print("+++++++++++")
imputer = SimpleImputer(missing_values = np.nan, strategy="mean")

imputer = imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])




