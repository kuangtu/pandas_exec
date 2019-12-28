# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np


def get_rank_num(array_v):
    """
    array_v: np.ndarray, 如 [1,2,3]
    return: 返回最后一个数在整个array_v的大小排名，以上行数据为例，返回为 3
    :param array_v:
    :return:
    """
    df = pd.DataFrame(array_v)
    # print(df)
    print(df.rank())
    return df.rank().iloc[-1, -1]

if __name__ == '__main__':
    array = [1, 4, 3]
    print(np.array(array))
    a = get_rank_num(np.array(array))
    print(a)