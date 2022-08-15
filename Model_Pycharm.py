import numpy as np
import pandas as pd

print('NumPy', np.__version__)
print('pandas', pd.__version__)

df_test = pd.read_csv("/home/cesarfernando/Cesar/Kaggle/Titanic/test.csv")
df_train = pd.read_csv("/home/cesarfernando/Cesar/Kaggle/Titanic/train.csv")
print(df_test.head)
print(df_train.head)

df_test.info()
df_train.info()
