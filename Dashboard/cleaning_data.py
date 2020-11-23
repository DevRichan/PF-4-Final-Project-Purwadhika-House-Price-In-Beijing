import pandas as pd 
import numpy as np
import seaborn as sns


def data_auto():
    df = pd.read_csv('clean_data')
    df.drop('Unnamed: 0',axis=1,inplace=True)
    return df

