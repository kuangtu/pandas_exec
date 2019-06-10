# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd


def countnum():
    dates = pd.date_range(start="2018-01-01", end="2019-12-31", freq='M')
    print(dates)
    print(dates[0])
    print(type(dates[0]))

if __name__ == '__main__':
    countnum()

