import pandas as pd
import numpy as np
import pandas as pd

df2 = pd.read_excel("Python Source\Python Source\excel-comp-data.xlsx")

df2.head(5).T

from pandas import DataFrame

A = pd.DataFrame()
rng = np.random.RandomState(42)
col_name = ["A", "B"]
df = pd.DataFrame(rng.randint(0, 10, (2,2)), columns=col_name)
print(df)
df1 = pd.DataFrame(rng.randint(0, 10, (3, 3)), columns=list("BAC"))


df1 = pd.DataFrame({"employee": ["Bob", "Jake", "Lisa", "Sue"],
                    "group": ["Accounting", "Enginerring", "Engineering", "HR"]})

df2 = pd.DataFrame({"employee": ["Lisa", "Bob", "Jake", "Sue"],
                    "hire_date": [2004, 2008, 2012, 2014]})

df3 = pd.merge(df1, df2)

df4 = pd.merge(df1, df2, on="employee")

print(df4)

df = pd.DataFrame({"group": ["Accounting", "Accounting", "Engineering", "Engineering", "HR", "HR",],
                   "skills": ["math", "spreadsheets", "coding", "Linux", "spreadsheets", "organization"]})

df6 = pd.DataFrame({"name": ["Peter", "Paul", "Mary"],
                    "food": ["fish", "beans", "brand"]},
                   columns=["name, food"])

df7 = pd.DataFrame({"name": ["Mary", "Joseph"],
                    "drink": ["wine", "beer"]},
                   columns=["name", "drink"])

pd.merge(df6, df7, on="name", how="right")