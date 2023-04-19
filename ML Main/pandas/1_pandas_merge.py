## Merge code example 
import pandas as pd
import numpy as np


#! ipython id=aecc234c40094e10a7b92d8c1df2c2e0
df1 = pd.DataFrame({"key": ["b", "b", "a", "c", "a", "b"],
                    "data1": pd.Series(range(6), dtype="Int64")})
df2 = pd.DataFrame({"key": ["a", "b", "a", "b", "d"],
                    "data2": pd.Series(range(5), dtype="Int64")})

#    key  data1  data2
# 0    b      0      1
# 1    b      0      3
# 2    b      1      1
# 3    b      1      3
# 4    a      2      0
# 5    a      2      2
# 6    c      3   <NA>
# 7    a      4      0
# 8    a      4      2
# 9    b      5      1
# 10   b      5      3


df3= pd.merge(df1, df2, on="key", how="left")
print(df3)


left = pd.DataFrame({"key1": ["foo", "foo", "bar"],
                     "key2": ["one", "two", "one"],
                     "lval": pd.Series([1, 2, 3], dtype='Int64')})
right = pd.DataFrame({"key1": ["foo", "foo", "bar", "bar"],
                      "key2": ["one", "one", "one", "two"],
                      "rval": pd.Series([4, 5, 6, 7], dtype='Int64')})

#   key1 key2  lval  rval
# 0  foo  one     1     4
# 1  foo  one     1     5
# 2  foo  two     2  <NA>
# 3  bar  one     3     6
# 4  bar  two  <NA>     7
pd.merge(left, right, on=["key1", "key2"], how="outer")



#   key1 key2  lval  rval
# 0  foo  one     1     4
# 1  foo  one     1     5
# 2  bar  one     3     6
pd.merge(left, right, on=["key1", "key2"], how="inner")




#   key1 key2_x  lval key2_y  rval
# 0  foo    one     1    one     4
# 1  foo    one     1    one     5
# 2  foo    two     2    one     4
# 3  foo    two     2    one     5
# 4  bar    one     3    one     6
# 5  bar    one     3    two     7
pd.merge(left, right, on="key1")


#   key1 key2_left  lval key2_right  rval
# 0  foo       one     1        one     4
# 1  foo       one     1        one     5
# 2  foo       two     2        one     4
# 3  foo       two     2        one     5
# 4  bar       one     3        one     6
# 5  bar       one     3        two     7
merge = pd.merge(left, right, on="key1", suffixes=("_left", "_right"))
print(merge)


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
pd.merge(left1, right1, left_on="key", right_index=True,  how="outer")








































