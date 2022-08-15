import numpy as np
import pandas as pd


df_test = pd.read_csv("/home/cesarfernando/Cesar/Kaggle/Titanic/test.csv")
df_train_oroginal = pd.read_csv("/home/cesarfernando/Cesar/Kaggle/Titanic/train.csv")

df_train_oroginal.info()
df_train = df_train_oroginal.copy()
del df_train['Cabin']
df_train=df_train.dropna(subset=['Age', 'Embarked'])
df_train.info()
col = ['Survived', 'Pclass', 'Sex', 'SibSp']
for i in col:
    print(df_train[i].unique())

women = df_train.loc[df_train.Sex == 'female']["Survived"]
male = df_train.loc[df_train.Sex == 'male']["Survived"]
#print(women.shape)
#print(sum(women))
#print(len(women))
#print(women)
rate_women = sum(women)/len(women)
rate_male = sum(male)/len(male)
print(rate_male*100, rate_women*100)

