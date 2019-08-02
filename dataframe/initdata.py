# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd


def create():
    empoyees = [('jack', 34, 'Sydney', 5),
                ('Riti', 31, 'Delhi', 7),
                ('Aadi', 16, np.NaN, 11),
                ('Mohit', 23, 'Delhi', 15),
                ('Veena', 33, 'Delhi', 4),
                ('Shaunak', 35, 'Mumbai', np.NaN),
                ('Shaun', 35, 'Colombo', 11)
                ]

    empDfObj = pd.DataFrame(
        empoyees, columns=[
            'Name', 'Age', 'City', 'Experience'], index=[
            'a', 'b', 'c', 'd', 'e', 'f', 'g'])

    print("Contents of the Dataframe : ")
    print(empDfObj)

def dict_df():
    perf_dict = {"code": ['000001', '000002', '000003'],
                 "close": [100, 91.1, 5.4],
                 "vol": [1000, 200, 3000]}

    df = pd.DataFrame(perf_dict)
    print(df)


if __name__ == '__main__':
    create()
    dict_df()
