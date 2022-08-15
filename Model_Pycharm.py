import numpy as np
import pandas as pd

#print('NumPy', np.__version__)
#print('pandas', pd.__version__)

df_test = pd.read_csv("/home/cesarfernando/Cesar/Kaggle/Titanic/test.csv")
df_train_oroginal = pd.read_csv("/home/cesarfernando/Cesar/Kaggle/Titanic/train.csv")

df_train_oroginal.info()
df_train = df_train_oroginal.copy()
del df_train['Cabin']
df_train=df_train.dropna(subset=['Age', 'Embarked'])
df_train.info()
