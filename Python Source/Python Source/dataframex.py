import numpy as np
import pandas as pd

arr = np.arange(8)

arr42 = arr.reshape((4,2))

arr24 = arr42.reshape((2,4))

ar1 = np.array([[1, 2, 3], [4, 5, 6]])
ar2 = np.array([[7, 8, 9], [10, 11, 12]])

mycon = np.concatenate([ar1, ar2], axis=0)
print(mycon)
mycon = np.concatenate([ar1, ar2], axis=1)
print(mycon)

varr = np.vstack((ar1, ar2))
print(varr)
harr = np.hstack((ar1, ar2))
print(harr)

myarr = np.random.randn(5, 2)
print(myarr)

d1, d2, d3 = np.split(myarr, [1, 3])
print(d1)
print(d2)
print(d3)

df1 = pd.DataFrame({"key": ["b", "b", "a", "c", "a", "b"],
					"data1": pd.Series(range(6), dtype="Int64")})
df2 = pd.DataFrame({"key": ["a", "b", "a", "b", "d"],
					"data2": pd.Series(range(5), dtype="Int64")})

df3 = pd.merge(df1, df2, on="key", how="outer")
print(df3)

left = pd.DataFrame({"key1": ["foo", "foo", "bar"],
					 "key2": ["one", "two", "one"],
					 "lval": pd.Series([1, 2, 3], dtype="int64")})

right = pd.DataFrame({"key1": ["foo", "foo", "bar", "bar"],
					 "key2": ["one", "one", "one", "two"],
					 "lval": pd.Series([4, 5, 6, 7], dtype="int64")})

print(pd.merge(left, right, on=["key1", "key2"], how="outer" ))

print(pd.merge(left, right, on=["key1", "key2"], how="inner" ))

print(pd.merge(left, right, on="key1", how="inner", suffixes=("_left", "_right") ))

left1 = pd.DataFrame({"key": ["a", "b", "a", "a", "b", "c"],
					  "value": pd.Series(range(6), dtype="Int64")})
right1 = pd.DataFrame({"group_val": [3.5, 7]}, index=["a", "b"])

print(pd.merge(left1, right1, left_on="key", right_index=True, how="outer"))

left1 = pd.DataFrame({"key": ["a", "b", "a", "a", "b", "c"],
                      "value": pd.Series(range(6), dtype="Int64")})
right1 = pd.DataFrame({"group_val": [3.5, 7]}, index=["a", "b"])


#   key  value  group_val
# 0   a      0        3.5
# 2   a      2        3.5
# 3   a      3        3.5
# 1   b      1        7.0
# 4   b      4        7.0
# 5   c      5        NaN
print(pd.merge(left1, right1, left_on="key", right_index=True,  how="outer"))