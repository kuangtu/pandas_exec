# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np

def checknull():

    # the seq 2 data is missing
    s =pd.Series([2, 3, np.nan, 7, 'the hobbit'])
    print(s)

    # test the null
    print(s.isnull())


    # check any missing values
    print(s.isnull().values.any())
    print(s.isnull().sum())


    # Count Missing Values in DataFrame
    df = pd.DataFrame(np.random.randn(5,5))
    df.columns = ['col1', 'col2', 'col3', 'col4', 'col5']
    df[df > 0.9] = np.nan

    #list each columns missing data sum
    print(df.isnull().sum())

if __name__ == '__main__':
    checknull()
