# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np

def initdf():
    start = '20190101'
    end = '20190110'
    dates = pd.date_range(start, end, freq='D')
    ndays = len(dates)

    price = np.random.randint(10, 15, ndays)
    df = pd.DataFrame({"code": "000001", "close": price}, index=dates)

    price = np.random.randint(20, 25, ndays)
    df = pd.DataFrame({"code": "000002", "close": price}, index=dates)

    price = np.random.randint(30, 35, ndays)
    df = pd.DataFrame({"code": "000003", "close": price}, index=dates)

    print(df.head())


if __name__ == '__main__':
    pd.set_option('expand_frame_repr', False)  # 显示所有列
    initdf()
