import numpy as np
import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')

# 상위 10개 레코드 
print(titanic.head(10))
print(titanic.groupby("sex")["survived"].mean())
print(titanic.groupby(["sex", "class"])["survived"].mean())
titanic.pivot_table("survived", index="sex", columns="class")
titanic.pivot_table("survived", index=["sex", "age"], columns="class")
																															#sum은 함수 mean 은 옵션
titanic.pivot_table(index="sex", columns="class", aggfunc={"survived": sum, "fare":"mean"})