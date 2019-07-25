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

def exponential_moving_average(df, n):
    '''
    指数移动平均线
    :param df:
    :param n:
    :return:
    '''
    EMA = pd.Series(df['Close'].ewm(span=n, min_periods=n).mean(), name='EMA' + str(n))
    df = df.join(EMA)

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

def momentum(df, n):
    '''

    :param df:
    :param n:
    :return:
    '''
    mom = pd.Series(df['Close'].diff(n), name='Momentum_' + str(n))
    df = df.join(mom)

    return df

if __name__ == '__main__':
    filename = "..\\data\\000001perf.csv"
    perf = load_perf(filename)

    perf_ma = moving_average(perf, 5)
    print(perf_ma.head())

    perf_ema = exponential_moving_average(perf, 5)
    print(perf_ema.head())