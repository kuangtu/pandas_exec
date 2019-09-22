# -*- coding: UTF-8 -*-
from pathlib import Path
import pandas as pd
import pandas_profiling
import requests
import numpy as np

def titanic_demo():
    # df = pd.read_csv(
    #     "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    # )
    # df.to_csv("..\\data\\titanic.csv")

    df = pd.read_csv("..\\data\\titanic.csv", index_col=0)
    print(df.head())
    report = pandas_profiling.ProfileReport(df)
    report.to_file(output_file=Path("titanic_report.html"))

def meteorities_demo():
    file_name = Path("..\data\\rows.csv")
    if not file_name.exists():
        data = requests.get(
            "https://data.nasa.gov/api/views/gh4g-9sfh/rows.csv?accessType=DOWNLOAD"
        )
        file_name.write_bytes(data.content)

    df = pd.read_csv(file_name)
    "转为日期类型"
    df['year'] = pd.to_datetime(df['year'], errors='coerce')
    df['boolean'] = np.random.choice([True, False], df.shape[0])
    df["mixed"] = np.random.choice([1, "A"], df.shape[0])
    df["reclat_city"] = df["reclat"] + np.random.normal(scale=5, size=(len(df)))
    duplicates_to_add = pd.DataFrame(df.iloc[0:10])
    duplicates_to_add[u"name"] = duplicates_to_add[u"name"] + " copy"
    df = df.append(duplicates_to_add, ignore_index=True)
    profile = pandas_profiling.ProfileReport(df,
             title="NASA Meteorites", correlation_overrides=["recclass"])
    profile.to_file(output_file=Path('meteorites.html'))


if __name__ == '__main__':
    # titanic_demo()
    meteorities_demo()

