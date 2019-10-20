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

def countnan():
    '''
    统计多个Nan数目
    :return:
    '''

    # 创建一个dataframe
    students = [('jack', np.NaN, 'Sydeny', 'Australia'),
                ('Riti', np.NaN, 'Delhi', 'India'),
                ('Vikas', 31, np.NaN, 'India'),
                ('Neelu', 32, 'Bangalore', 'India'),
                ('John', 16, 'New York', 'US'),
                ('John', 11, np.NaN, np.NaN),
                (np.NaN, np.NaN, np.NaN, np.NaN)
                ]
    # Create a DataFrame object
    dfObj = pd.DataFrame(students, columns=['Name', 'Age', 'City', 'Country'])
    print(dfObj)

    # 统计df中Nan是否有null，单元格中返回False或者True
    # 只包含了True或者False
    print(dfObj.isnull())

    # 按照列进行检查
    print(dfObj.isnull().sum())

    # 统计整个的df
    print(dfObj.isnull().sum().sum())

    # 统计每行的缺失
    for i in range(len(dfObj.index)):
        # 通过iloc取出了一行，返回了该行的Series
        print("Nan in Row", i, ":", dfObj.iloc[i].isnull().sum())

if __name__ == '__main__':
    # checknull()

    countnan()