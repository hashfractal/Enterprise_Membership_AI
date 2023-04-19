
import numpy as np 

# [0 1 2 3 4 5 6 7]
arr = np.arange(8)
print(arr)

# [[0 1]
#  [2 3]
#  [4 5]
#  [6 7]]
arr1=arr.reshape((4, 2))
print(arr1)

#A multidimensional array can also be reshaped:
# [[0 1 2 3]
#  [4 5 6 7]]
arr3 = arr.reshape((4, 2)).reshape((2, 4))
print(arr3)



#One of the passed shape dimensions can be –1, in which case the value used for that
#dimension will be inferred from the data:
import numpy as np
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])

# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]
con1 = np.concatenate([arr1, arr2], axis=0)
print(con1)

# [[ 1  2  3  7  8  9]
#  [ 4  5  6 10 11 12]]
con2 = np.concatenate([arr1, arr2], axis=1)
print(con2)

# There are some convenience functions, like vstack and hstack, for common kinds of
# concatenation. The preceding operations could have been expressed as:
varr = np.vstack((arr1, arr2))
print(varr)
harr = np.hstack((arr1, arr2))
print(harr)

#split
# [[ 0.45713811  1.88478509]
#  [ 0.22840846  1.77375991]
#  [ 1.01523565  0.27123928]
#  [ 0.8467038   1.45810376]
#  [-0.22959047 -1.97743302]]
arr = np.random.randn(5, 2)
print(arr)


#seperate ndarray as first second and third
# first
# [[0.45713811 1.88478509]] 

#second
# [[0.22840846 1.77375991]
#  [1.01523565 0.27123928]] 

#third
# [[ 0.8467038   1.45810376]
#  [-0.22959047 -1.97743302]] 
first, second, third = np.split(arr, [1, 3])
print(first,"\n")
print(second,"\n")
print(third,"\n")


