# -*- coding: UTF-8 -*-
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

nums = np.array([1, 2, 3, 4, 5, 4, 5, 3])
print(nums)
# 分为3个分位
counts = pd.cut(nums, 3).value_counts()
print(counts)

plt.figure(figsize=(14, 4))
sns.barplot(x=np.arange(0, len(counts)),
            y=counts.values)
plt.show()

