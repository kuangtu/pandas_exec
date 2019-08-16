# -*- coding: UTF-8 -*-
import pandas as pd

date_start = pd.period_range(start='20170101', end='20190630', freq='Y')
print(date_start)
# 得到年初的日期
print(date_start.to_timestamp())
# 得到年末的日期
print(date_start.to_timestamp(how='end'))



