# -*- coding: UTF-8 -*-
# https://mp.weixin.qq.com/s/3Le5wsVcMD7BRo00VB9T_w
import numpy as np
import pandas as pd
import seaborn as sns

df = sns.load_dataset('titanic')
print(df.columns)
print(df.head())

# 删除部分数据
df.drop(columns=["who","adult_male","deck","embark_town","alive","alone","class"], inplace=True)

# 缺失值处理
df = df[df["embarked"].notnull()]
df['age'].fillna(df['age'].mean(), inplace=True)

# 年龄分段
df['age'] = pd.cut(df['age'], [0, 18, 90])

print(df.head())

# 查看不同性别的存活率
table = pd.pivot_table(df, index=['sex'], values='survived')
print(table)

#df是要传入的数据；

#index是 Values to group by in the rows，也就是透视表建立时要根据哪些字段进行分组，我们这里只依据性别分组；

#values是指对哪些字段进行聚合操作，因为我们只关心不同性别下的存活率情况，所以values只需要传入一个值"survived"；

#将所有乘客按性别分为男、女两组后，对"survived"字段开始进行聚合，默认的聚合函数是"mean"，也就是求每个性别组下所有成员的"survived"的均值，即可分别求出男女两组各自的平均存活率。

# 添加一个列级分组索引：pclass客票级别
table = pd.pivot_table(df, index=['sex'], columns=['pclass'], values='survived')
print(table)
print(table.columns)
print(table.index)

# 多级行索引
table = pd.pivot_table(df, index=['sex', 'pclass'], values='survived')
print(table)

# 多级列索引
table = pd.pivot_table(df, index=['sex'], columns=['pclass', 'age'], values='survived')
print(table)

# 多个聚合列
table = pd.pivot_table(df, index=['pclass'], values=['survived', 'fare'])
print(table)

# 自定义聚合函数
# 指定聚合函数
table = pd.pivot_table(df, index=["pclass"], values=["survived", "fare"], aggfunc=["mean", sum, "count"])
print(table)

#聚合函数支持常见的统计函数，如"mean", "sum", count, np.mean, np.std, np.corr等，支持字符串等多种格式。
#如果传入参数为list，则每个聚合函数对每个列都进行一次聚合。
#如果传入参数为dict，则每个列仅对其指定的函数进行聚合,此时values参数可以不传

# aggfunc传入字典类型，自定义每个列要适用的聚合函数
table = pd.pivot_table(df, index=["pclass"], aggfunc={"survived": ["mean", sum], "fare": ["count", np.std]})
print(table)

# 添加汇总项
# 按行、按列进行汇总，指定汇总列名为“Total”,默认名为“ALL”
table1 = pd.pivot_table(df, index="sex", columns="pclass", values="survived", aggfunc= "count", margins=True, margins_name="Total")
print(table1)
