# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np

def initdf():
    start = '20190101'
    end = '20190110'
    dates = pd.date_range(start, end, freq='D')
    ndays = len(dates)

    stock = pd.DataFrame()
    price = np.random.randint(10, 15, ndays)
    pct = np.random.uniform(0, 1, ndays)
    df = pd.DataFrame({"code": "000001", "close": price, "pct": pct}, index=dates)
    stock = stock.append(df)

    price = np.random.randint(20, 25, ndays)
    pct = np.random.uniform(0, 1, ndays)
    df = pd.DataFrame({"code": "000002", "close": price, "pct": pct}, index=dates)
    stock = stock.append(df)

    price = np.random.randint(30, 35, ndays)
    pct = np.random.uniform(0, 1, ndays)
    df = pd.DataFrame({"code": "000003", "close": price, "pct": pct}, index=dates)
    stock = stock.append(df)

    # 按照单个字段进行分组，然后计算
    # 计算过程是df
    grouped = stock.groupby('code')
    # print(type(grouped[['close']].mean()))
    # print(grouped[['close']].mean())

    # 计算过程是Series
    # print(type(grouped['close'].mean()))
    # print(grouped['close'].mean())


    # 得到最大、最小值
    # print(grouped['close'].max())
    # print(grouped['close'].min())
    #
    # print(grouped[['close']].max())
    # print(grouped[['close']].min())

    stock_copy = stock.copy()
    stock_copy.reset_index(inplace=True)
    stock_copy.rename(columns={'index': 'tradeDate'}, inplace=True)
    # stock_copy.set_index('tradeDate', drop=True, inplace=True)
    # 按照多个键进行分组聚合
    # grouped = stock_copy.groupby(['code', 'tradeDate'])
    # print(grouped['close'].count())
    # 如果是df，输出的是整个df
    # print(grouped[['close']].count())

    # 不带入索引（可以理解为重置索引）
    #  输出了整个df
    grouped = stock_copy.groupby(['code', 'tradeDate'], as_index=False)
    print(grouped['close'].count())

    # 一次应用多个聚合函数
    aggregated = grouped['close'].agg(['max', 'min'])
    print(aggregated)

    #列为MultiIndex
    print(aggregated.columns)
    print(type(aggregated.columns))

    # 不同列应用不同的聚合函数
    def spread(series):
        return series.max() - series.min()

    aggregator = {"close": "mean", 'pct': spread}
    aggregated = grouped.agg(aggregator)
    print(aggregated)


    #apply应用，分组之后应用
    def top(df, column='close'):
        return df.sort([column])[-1:]


    grouped = stock_copy.groupby('code', as_index=False, group_keys=False).apply(top)
    print(grouped)

if __name__ == '__main__':
    pd.set_option('expand_frame_repr', False)  # 显示所有列
    initdf()
