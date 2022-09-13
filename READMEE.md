# Titanic Project, data exploration and data modeling

<img src = "Images/RMS_Titanic_3.jpg" width = 300 height = 200>

<!--![Images](Images/RMS_Titanic_3.jpg)-->

## Sections

- [Titanic Project, data exploration and data modeling](#titanic-project-data-exploration-and-data-modeling)
  - [Sections](#sections)
    - [Data adquisition](#data-adquisition)
    - [Data exploration](#data-exploration)
    - [Data preproccesing](#data-preproccesing)

### Data adquisition

- The Data set was adquired via kaggle reposities and challengers.
  - [kaggle.com](https://www.kaggle.com/competitions/titanic "Titanic Data Set")
- It was stored in a local device and sync via GitHub.
  - [GitHub_Repository](https://github.com/Cesar421/Titanic "Cesar GitHub")
  
### Data exploration

Here we start the exploration of the data,

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
