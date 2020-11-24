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
   - Fill in the missing values
   - Performing Column II Check (Checking Column Data Types) Because there is data missing, so there are several columns whose data types cannot be changed, therefore I checked and changed them again.

- **Exploratory Data Analysis:**
  - Territorial and population information
  - Correlation of Other Columns with Column Target (TotalPrice) / subject that affects the price
  
- **Modelling**
  - In this modeling, two jobs are carried out, namely data with outliers and data without outliers, and using 5 machine learning algorithms along with hyperparameter tuning. At the time of tuning I had problems, namely low computer specs, and Google Colab which was always an error due to the many tuning parameters and data, so I divided the random forest tuning into 3 parts. 
  - Machine Learning 1 Notebook files are machine learning files with outlier data, and Machine Learning 2 files are machine learning files whose outlier data is deleted.



### Vital Records:
I have difficulty training the model due to low computer specs, I've tried using Google Colab but the results are the same maybe because I subscribed for free. Therefore, the model is not optimal. My advice if you want to continue this work use a random forest algorithm and multiply the tuning parameters, or you can try using other algorithms like SVM, KNN etc.





### Dashboard : 



