# -*- coding: UTF-8 -*-
import pandas as pd

def mean_test():
    df = pd.DataFrame({"000001": [10,11,12,13],
                       "000002": [20,21,22,23]})
    print(df)

    rt = df.mean()
    print(rt)

    rt = df.mean(axis=1)
    print(rt)



if __name__ == '__main__':
    mean_test()