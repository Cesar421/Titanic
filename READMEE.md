# Titanic Project, data exploration and data modeling

<img src = "Images/RMS_Titanic_3.jpg" width = 300 height = 200>

<!--![Images](Images/RMS_Titanic_3.jpg)-->

## Sections

- [Titanic Project, data exploration and data modeling](#titanic-project-data-exploration-and-data-modeling)
  - [Sections](#sections)
    - [Libraries and tools used](#libraries-and-tools-used)
    - [Data adquisition](#data-adquisition)
    - [Data exploration](#data-exploration)
    - [Data preproccesing](#data-preproccesing)

### Libraries and tools used

```python
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from termcolor import colored
import seaborn as sns
import warnings
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn import linear_model
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
warnings.simplefilter('ignore')
import platform
platform.system()
```

### Data adquisition

- The Data set was adquired via kaggle reposities on challenger chapter.
  - [kaggle.com](https://www.kaggle.com/competitions/titanic "Titanic Data Set")
- It was stored in a local device and sync via GitHub.
  - [GitHub_Repository](https://github.com/Cesar421/Titanic "Cesar GitHub")
  
### Data exploration

Here we start the exploration of the data,

This is the .describe info of train data set

| **_#_**  | **_Column_**  | **_Non-Null Count_**  | **_Dtype_**  |  
|:-------: |:------------: |:--------------------: |:-----------: |
|  **0**   |  PassengerId  |     891 non-null      |    int64     |
|  **1**   |   Survived    |     891 non-null      |    int64     |
|  **2**   |    Pclass     |     891 non-null      |    int64     |
|  **3**   |     Name      |     891 non-null      |    object    |
|  **4**   |      Sex      |     891 non-null      |    object    |
|  **5**   |      Age      |     714 non-null      |   float64    |
|  **6**   |     SibSp     |     891 non-null      |    int64     |
|  **7**   |     Parch     |     891 non-null      |    int64     |
|  **8**   |    Ticket     |     891 non-null      |    object    |
|  **9**   |     Fare      |     891 non-null      |   float64    |
|  **10**  |     Cabin     |     204 non-null      |    object    |
|  **11**  |   Embarked    |     889 non-null      |    object    |

```python
def createFeatureClass(self, location, name, excludeFields=[]):
```

### Data preproccesing

- #### Numerical variables
  
- #### Categorical variables
