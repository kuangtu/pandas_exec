# -*- coding: UTF-8 -*-
# https://jakevdp.github.io/PythonDataScienceHandbook/03.05-hierarchical-indexing.html

import pandas as pd
import  numpy as np

# Series多索引
index = [('California', 2000), ('California', 2010),
         ('New York', 2000), ('New York', 2010),
         ('Texas', 2000), ('Texas', 2010)]
populations = [33871648, 37253956,
               18976457, 19378102,
               20851820, 25145561]
pop = pd.Series(populations, index=index)
print(pop)

# 按照索引或者序号访问
print(pop[('California', 2010):('Texas', 2000)])
print(pop[0:1])
# 索引为tuple中的第2个元素
print(pop[[i for i in pop.index if i[1] == 2010]])


# 基于多索引方式
index = pd.MultiIndex.from_tuples(index)
print(index)

# 多个索引，此时pop还是Series
pop = pop.reindex(index)
print(type(pop))
print(pop)

# 此时可以按照多个索引访问，索引间通过","分隔，支持序列
print(pop[:,2000])
print(pop["California",])

# unstack() 将多索引的Series转为Dataframe
pop_df = pop.unstack()
print(pop_df)

# 相反,stack()
pop_df = pop_df.stack()
print(pop_df)

# 多索引的Series
print(type(pop))
pop_df = pd.DataFrame({'total': pop,
                       'under18': [9267089, 9284094,
                                   4687374, 4318033,
                                   5906301, 6879014]})
print(pop_df)
f_u18 = pop_df['under18'] / pop_df['total']
# 得到了多个索引的Series
print(f_u18)
print(f_u18.unstack())


# 多索引创建df
df = pd.DataFrame(np.random.rand(4, 2),
                  index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns=['data1', 'data2'])
print(df)

#多索引建立
# codes中对于数据的levels索引下标进行了标注
mulidx = pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b'], [1, 2, 1, 2]])
print(mulidx)

# 设置多索引名称
pop.index.name = ['state', 'year']
print(pop)


# 列的多级索引
# 多级index
# hierarchical indices and columns
index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]],
                                   names=['year', 'visit'])
# 此时from_product，索引为A*B方式
columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], ['HR', 'Temp']],
                                     names=['subject', 'type'])
# mock some data
data = np.round(np.random.randn(4, 6), 1)
data[:, ::2] *= 10
data += 37
# create the DataFrame
health_data = pd.DataFrame(data, index=index, columns=columns)
print(health_data)

# 按照列访问
print(health_data['Guido'])
# 在此访问其中的列
print(health_data['Guido', 'HR'])

# 按照iloc访问，
print(health_data.iloc[:3,:3])
# 按照loc访问
print(health_data.loc[2013,:])
print(health_data.loc[(2013,1),:].unstack())

