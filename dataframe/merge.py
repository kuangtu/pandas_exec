# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np

def crttwodf_diff():
    startDate = "20190101"
    endDdate = "20190106"
    dates = pd.date_range(startDate, endDdate, freq='D')
    perf = pd.DataFrame({"tradeDate": dates})

    # add ticker and price
    perf['ticker'] = '000003'
    values = np.random.random_integers(30, 32, len(dates))
    perf['close'] = values

    return perf


def crttwodf():
    startDate = "20190101"
    endDdate = "20190105"
    dates = pd.date_range(startDate, endDdate, freq='D')
    perf = pd.DataFrame({"tradeDate": dates})

    # add ticker and price
    perf['ticker'] = '000001'
    values = np.random.random_integers(10, 12, len(dates))
    perf['close'] = values

    perf2 = pd.DataFrame({"tradeDate": dates})
    # add ticker and price
    perf2['ticker'] = '000002'
    values = np.random.random_integers(20, 22, len(dates))
    perf2['close'] = values

    return perf, perf2

def concat_test():
    # 按照行或者列进行拼接 axis=0 按照行, axis=1按照列
    df1, df2 = crttwodf()
    df3 = pd.concat([df1, df2], axis=0, ignore_index=True)
    print(df3)

    # 按照列方式拼接，此时没有参数ignore_index
    df1, df2 = crttwodf()
    df4 = pd.concat([df1, df2], axis=1)
    print(df4)

    # 如果按照列方式拼接，索引位置没有值的会填充NaN
    df1, df2 = crttwodf()
    df5 = crttwodf_diff()

    # df1 缺失了索引为2019-01-06的行，通过Nan填充
    df6 = pd.concat([df1, df5], axis=1)
    print(df6)

    # 通过join方式设置合并的方式
    # join = 'inner'，选择有相同索引的行情
    df1, df2 = crttwodf()
    df5 = crttwodf_diff()
    df7 = pd.concat([df1, df5], axis=1, join='inner')
    print(df7)


def append_test():
    df1, df2 = crttwodf()
    # print(df1.head())
    # print(df2.head())

    # 上下拼接，追加，
    # 通过ignore_index重置索引
    df1 = df1.append(df2, ignore_index=True)
    print(df1)

def merge_test():
    df1, df2 = crttwodf()

    # how选择不同的连接方式
    # on按照列中的值进行合并
    # 操作会自动为合并前有相同列名、不同值的列名添加后缀

    df3 = pd.merge(df1, df2, how='inner', on='tradeDate', sort=True)
    print(df3)

    # 通过suffix增加后缀名称
    suffix = []
    suffix.append(df1.ticker.unique()[0])
    suffix.append(df2.ticker.unique()[0])
    print(suffix)
    df4 = pd.merge(df1, df2, how='inner', on='tradeDate', sort=True, suffixes=suffix)
    print(df4)

    # 如果需要合并的列不同，则可以使用left_on和right_on指定要进行合并的列名
    df5, df6 = crttwodf()
    df5.rename(columns={'tradeDate': 'tradeDate1'}, inplace=True)
    df7 = pd.merge(df5, df6, left_on='tradeDate1', right_on='tradeDate', how='inner', sort=True, suffixes=suffix)
    print(df7)

    #也可以通过on设置需要制定的列
    df8, df9 = crttwodf()
    df10 = pd.merge(df8, df9, on=['tradeDate'], how='inner', sort=True, suffixes=suffix)
    print(df10)

if __name__ == '__main__':
    # append_test()
    # concat_test()
    merge_test()