# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np

def series_save_csv():

    #create series
    dates = pd.date_range(start='20190101', end='20190110')
    dates_lens = len(dates)
    close = np.random.randint(10, 12, dates_lens)
    print(close)

    close_series = pd.Series(close, index=dates, name='close')
    close_series.rename(index='Dates')
    print(close_series)
    print(close_series.name)
    print(close_series.index)

    #通过index_label增加 index的名称
    close_series.to_csv("..\\data\\series_to_csv.csv", header=True, index_label='Date')

def series_to_dataframe():
    #create series
    dates = pd.date_range(start='20190101', end='20190110')
    dates_lens = len(dates)
    close = np.random.randint(10, 12, dates_lens)
    close_series = pd.Series(close, index=dates, name='close')
    close_series.rename(index='Dates')

    vol = np.random.randint(100000, 110000, dates_lens)
    vol_series = pd.Series(vol, index=dates, name='vol')

    # merge to dataframe
    df = pd.concat([close_series, vol_series], axis=1)
    print(df.head())


def csv_to_series():

    # pd.Series.from_csv 太旧了
    close_df = pd.read_csv("..\\data\\series_to_csv.csv", index_col=0)
    close_series = close_df['close']
    print(type(close_series))
    print(close_series)


# series_save_csv()

# series_to_dataframe()

# csv_to_series()





