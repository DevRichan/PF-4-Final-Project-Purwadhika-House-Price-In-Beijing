import pickle
from pandas import DataFrame, get_dummies

model = pickle.load(open('finalized_model.sav','rb'))
one_hot_columns = pickle.load(open('x_dummies_column.sav','rb'))

def prediction_data(data):
    df = DataFrame(data,index=[0])
    df = get_dummies(df)
    dftmp = get_dummies(df)
    df = df.reindex(columns=one_hot_columns, fill_value = 0)
    hasil = model.predict(df)
    hasil2 = model.feature_importances_
    return round(hasil[0])
    # hasil2 = DataFrame(hasil2,index=df.columns)
    # return hasil2.sort_values(by=0,ascending=False)

def feature_importances(data):
    df = DataFrame(data,index=[0])
    df = get_dummies(df)
    dftmp = get_dummies(df)
    df = df.reindex(columns=one_hot_columns, fill_value = 0)
    hasil = model.predict(df)
    hasil2 = model.feature_importances_
    hasil2 = DataFrame(hasil2,index=df.columns)
    return hasil2.sort_values(by=0,ascending=False)
    

