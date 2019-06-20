# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np

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

if __name__ == '__main__':
