# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def copywarning_fix():
   movies = pd.read_csv("..\\data\\movies.csv", index_col=0)
   # movies = pd.read_csv("http://bit.ly/imdbratings")
   # movies = pd.read_csv("https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/imdb_1000.csv")
   # movies.to_csv("..\\data\\movies.csv", index_label='seq')
   # print(movies.head())

   print(movies.head())

   # missing = movies.content_rating.isnull().sum()
   # print (missing)

   # print (movies[movies.content_rating.isnull()])


   # print(movies.content_rating.value_counts())

   print(movies[movies.content_rating == 'NOT RATED'].content_rating)

   # 出现了SettingWithCopyWarning:
   # 此时赋值是没有效果的
   # movies[movies.content_rating == 'NOT RATED'].content_rating = np.nan
   # missing = movies.content_rating.isnull().sum()
   # print (missing)


   movies.loc[movies.content_rating == 'NOT RATED', 'content_rating'] = np.nan
   # missing = movies.content_rating.isnull().sum()
   # print (missing)

   top_movies = movies.loc[movies.star_rating >= 9, :]
   print(top_movies)

   # top_movies.loc[0, 'duration'] = 150
   # print(top_movies)

   top_movies = movies.loc[movies.star_rating >= 9, :].copy()
   top_movies.loc[0, 'duration'] = 150





if __name__ == '__main__':
   copywarning_fix()