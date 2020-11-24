# Housing price in Beijing
### Housing price of Beijing from 2011 to 2017, fetching from Lianjia.com. 
The dataset can be downloaded at https://www.kaggle.com/ruiqurm/lianjia

### I. About Beijing : 
<p align="justify"><b>Beijing</b> is the capital of the People's Republic of China and one of the
                    the most populous city in the world with a population of over 21 million. The metropolis that is located
                    in northern China it is a municipality under the direct control of the Chinese central government
                    consisting of 16 urban, suburban and rural districts. As a megacity, Beijing is the second largest city in China after Shanghai in terms of
                    The number of urban residents, the rest of Beijing is the center of national politics, culture and education.
                    Beijing is home to the world's four largest financial institutions and major corporations
                    Chinese-owned state-owned enterprises and home to a number of world-class companies on the annual list
                    Fortune Global 500. Beijing is also a major center, the national highway, the expressway
                    controlled, rail lines and high speed rail network. Beijing Capital International Airport
                    being the second busiest airport in the world based on heavy passenger traffic since 2010 and
                    The Beijing subway is the world's busiest and longest subway network as of 2016.  


### II. Goals : 
- Build machine learning to predict house prices in beijing

### III. Work Steps : 
- **Data Preparation :**
   - Peforming Columns I Check (Checking Column and Column related Data)
   - Converting Categorical Numeric Values to Strings.
   - Fill in The Missing Values
   - Performing Column II Check (Checking Column Data Types) Because there is data missing, so there are several columns whose data types cannot be changed, therefore I checked and changed them again.

- **Exploratory Data Analysis:**
  - Territorial and Population Information
  - Correlation of Other Columns with Column Target (TotalPrice) / Subject That Affects The Price
  
- **Modelling**
  - In this modeling, two jobs are carried out, namely data with outliers and data without outliers, and using 5 machine learning algorithms along with hyperparameter tuning. At the time of tuning I had problems, namely low computer specs, and Google Colab which was always an error due to the many tuning parameters and data, so I divided the random forest tuning into 3 parts. 
  - Machine Learning 1 Notebook files are machine learning files with outlier data, and Machine Learning 2 files are machine learning files whose outlier data is deleted.


### Vital Records:
I have difficulty training the model due to low computer specs, I've tried using Google Colab but the results are the same maybe because I subscribed for free. Therefore, the model is not optimal. My advice if you want to continue this work use a random forest algorithm and multiply the tuning parameters, or you can try using other algorithms like SVM, KNN etc.

### Model Training Results :
This is the result of machine learning training with outliers data, I am not displaying machine learning results whose outliers have been removed because the results are so poor.

No  |  Algoritma  | RMSE |
------|--------|---------------|
1 |   Linear Regression Default Parameter |  145.47390826021032 |
2 |   Ridge Regression Default Parameter |   145.4739284326783 |
3 |   Lasso Regression Default Parameter |   145.4680170558296 |
4 |   Decison Tree Regressor Default Parameter |   159.2454346602503 |
5 |   Decison Tree Regressor with Parameter|   139.41951268165724 |
6 |   Random Forest Regressor Default Parameter |   126.96117847547191 |
7 |   Random Forest Regressor with Parameter I |   124.62968428056467 |
8 |   Random Forest Regressor with Parameter II |   124.3104488455155|
9 |   Random Forest Regressor with Parameter III |   125.18869710930282|

The Random Forest Regressor with Parameter II has the lowest RMSE value compared to other models. It can be seen that the regplot graph shows pretty good results, but this model cannot be said to be optimal. Therefore, I suggest doing model training by adding parameters to the hyperparameter tuning and trying to use another model.

Details of model training (Random Forest with Parameter II):

- Amount of data: 316448
- Training data: 90%
- Test Data: 10%
- Algorithm: Random Forest Regressor
- Standardized Value: Robust Scaller
- The training method used: GridSearch CV
- Best parameters: {'max_depth': None, 'min_samples_leaf': 5, 'min_samples_split': 6, 'n_estimators': 120}



### Dashboard : 
[Final Project Purwadhika - House Price In Beijing - Ricki Chandra Hidayatullah](https://www.youtube.com/watch?v=abENDgwcclQ&ab_channel=RickiChandraHidayatullah)






