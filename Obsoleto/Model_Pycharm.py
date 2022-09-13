import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

df_test = pd.read_csv("/home/cesarfernando/Cesar/Kaggle/Titanic/test.csv")
df_train_original = pd.read_csv("/home/cesarfernando/Cesar/Kaggle/Titanic/train.csv")

df_train_original.info()
df_train = df_train_original.copy()
del df_train['Cabin']
df_train = df_train.dropna(subset=['Age', 'Embarked'])
df_train.info()
col = ['Survived', 'Pclass', 'Sex', 'SibSp']
for i in col:
    print(df_train[i].unique())

women = df_train.loc[df_train.Sex == 'female']["Survived"]
male = df_train.loc[df_train.Sex == 'male']["Survived"]

rate_women = sum(women)/len(women)
rate_male = sum(male)/len(male)
print(rate_male*100, rate_women*100)

y = df_train["Survived"]

features = ["Pclass", "Sex", "SibSp", "Parch"]
X = pd.get_dummies(df_train[features])
X_test = pd.get_dummies(df_train[features])

model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X, y)
predictions = model.predict(X_test)

output = pd.DataFrame({'PassengerId': df_test.PassengerId, 'Survived': predictions})
output.to_csv('my_submission.csv', index=False)
print("Your submission was successfully saved!")
