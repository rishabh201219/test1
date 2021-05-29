import numpy as np
import pandas as pd
import seaborn as sns
#import matplotlib.pyplot as plt 


from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

#def preprocess_origin_cols(df):
   # df['Origin'] = df['Origin'].map({1: "india", 2: "usa", 3: "germany"})
   # return df

acc_ix,hpower_ix,cyl_ix=4,2,0
class CustomAttrAdder(BaseEstimator,TransformerMixin):
    def __init__(self,acc_on_power=True):
        self.acc_on_power=acc_on_power
    def fit(self,x,y=None):
        return self
    def transform(self,x):
        acc_on_cyl=x[:,acc_ix]/x[:,cyl_ix]
        if self.acc_on_power:
            acc_on_power=x[:,acc_ix]/x[:,hpower_ix]
            return np.c_[x,acc_on_cyl,acc_on_power]
        return np.c_[x,acc_on_cyl]


def num_pipeline_transformer(data):
    '''
    Function to process numerical transformations
    Argument:
        data: original dataframe 
    Returns:
        num_attrs: numerical dataframe
        num_pipeline: numerical pipeline object
        
    '''
    numerics = ['float64', 'int64']

    num_attrs = data.select_dtypes(include=numerics)

    num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy="median")),
        ('attrs_adder', CustomAttrAdder()),
        ('std_scaler', StandardScaler()),
    ])
    return num_attrs, num_pipeline

def pipeline_transformer(data):
  
    cat_attrs = ["Origin"]
    num_attrs, num_pipeline = num_pipeline_transformer(data)

    full_pipeline = ColumnTransformer([
        ("num", num_pipeline, list(num_attrs)),
        ("cat", OneHotEncoder(), cat_attrs)
    ])
    prepared_data = full_pipeline.fit_transform(data)
    return prepared_data


def predict_mpg(config, model):

    list=['Cylinders','Displacement','Horsepower','Weight','Acceleration','model_year','Origin']
    con={}
    for key in list:
        for value in config:
            con[key] = value
            config.remove(value)
            break  
   
    
    if type(con) == dict:
        df = pd.DataFrame(con)

    else:
        df = con

    #preproc_df = preprocess_origin_cols(df)
    df["Origin"] = df["Origin"].replace({1: "india", 2: "usa", 3: "germany"})
    prepared_df = pipeline_transformer(df)
    y_pred = model.predict(prepared_df)
    return y_pred

