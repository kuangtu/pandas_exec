# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np
# panel看做pandas容器，三维结构。其中:
# （1）items - axis 0，内部包含了dataframe
# （2）major_axis - axis 1，每个dataframe中的索引行
# （3）minor_axis - axis 2，每个dataframe中的列，
# 但是之后会弃用，基于多索引方式。


p = pd.Panel(np.arange(24).reshape(4,3,2),
            items=list('abcd'),
            major_axis=pd.date_range('20130101', periods=3),
            minor_axis=['first', 'second']
             )

print(p)
# 此时一共有a,b,c,d 四个item，分别对应了每个dataframe，
# 而每个dataframe是3*2结构，索引为日期，列为minor_axis
print(p['a'])

# 按照行索引访问
# 此时得到dataframe，索引为minor_axis，列为items
print(p.major_xs('2013-01-01'))

