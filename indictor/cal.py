# -*- coding: UTF-8 -*-

import pandas as pd

def moving_average(df, n):
    """Calculate the moving average for the given data.

    :param df: pandas.DataFrame
    :param n:
    :return: pandas.DataFrame
    """
    MA = pd.Series(df['Close'].rolling(n, min_periods=n).mean(), name='MA_' + str(n))
    df = df.join(MA)
    return df

def load_perf(filename):
    '''
    load the perf
    :param filename:
    :return:
    '''
    tmp = pd.read_csv(filename, encoding='gbk', index_col=0)
    tmp.rename(columns={'closePrice': 'Close'}, inplace=True)
    print(tmp.head())

    return tmp

if __name__ == '__main__':
    filename = "..\\data\\000001perf.csv"
    perf = load_perf(filename)

    perf_ma = moving_average(perf, 5)
    print(perf_ma.head())