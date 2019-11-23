# -*- coding: UTF-8 -*-
import pandas as pd

def find_max():
    perf_dict = {"code": ['000001', '000002', '000003'],
                 "close": [100, 91.1, 5.4],
                 "vol": [1000, 200, 3000]}

    df = pd.DataFrame(perf_dict)
    print(df)
    max = df.loc[(df['close'].idxmax())]
    print(max)


if __name__ == '__main__':
    find_max()