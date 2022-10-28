from sklearn.impute import SimpleImputer
import numpy as np
import pandas as pd
from sklearn.preprocessing import *
from sklearn.compose import make_column_transformer
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as seabornInstance 
import sklearn.model_selection 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics



df = pd.read_csv("runners.csv")
df.head()





