# -*- coding: UTF-8 -*-
import pandas as pd

def cumsum_test():
    df = pd.DataFrame({"A": [5, 3, 6, 4],
                       "B": [11, 2, 4, 3],
                       "C": [4, 3, 8, 5],
                       "D": [5, 4, 2, 8]})
    print(df)

    #按照行进行相加
    print(df.cumsum(axis=0))

    # 按照列进行相加
    print(df.cumsum(axis=1))

def cumprod_test():
    df = pd.DataFrame({"A": [5, 3, 6, 4],
                       "B": [11, 2, 4, 3],
                       "C": [4, 3, 8, 5],
                       "D": [5, 4, 2, 8]})

    print(df)

    # 按照行相乘
    print(df.cumprod(axis=0))

    # 按照列相乘
    print(df.cumprod(axis=1))


if __name__ == '__main__':
    cumsum_test()
    cumprod_test()
