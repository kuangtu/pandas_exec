# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd


def countnum():
    dates = pd.date_range(start="2019-01-01", end="2019-05-31", freq='M')
    # print(dates)
    # print(dates[0])
    # print(type(dates[0]))
    col1 = [i for i in range(1, len(dates) + 1)]
    # print(col1)
    col2 = [i + 1 for i in range(1, len(dates) + 1)]

    df = pd.DataFrame({'col1': col1, 'col2': col2}, index=dates)
    # print(df)

    dict_ic = {}
    dict_ic['date'] = df
    df_ic = pd.concat(dict_ic.values(), keys=dict_ic.keys())
    # print (df_ic)

    # 基于list统计
    mean = df_ic.groupby(level=0).apply(lambda frame: len(
        [i for i in frame['col1'].values if i > 2]) / len(frame['col1']))
    print(mean)

def statfunc():
    perf_dict = {"code": ['000001', '000002', '000003'],
                 "close": [100, 91.1, 5.4],
                 "vol": [1000, 200, 3000]}

    df = pd.DataFrame(perf_dict)
    #最大、最小值所在位置
    print(df['close'].idxmin())
    min_close = df.iloc[df['close'].idxmin(),:]
    print(min_close)

    max_close = df.iloc[df['close'].idxmax(), :]
    print(max_close)

    result = df.any(axis=0)
    print(result)

if __name__ == '__main__':
    # countnum()
    statfunc()
