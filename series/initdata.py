# -*- coding: UTF-8 -*-
import pandas as pd

def init_series():
    series = pd.Series(data=[], index=[])
    series['a'] = 1
    series['b'] = 2
    print(series)


if __name__ == '__main__':
    init_series()