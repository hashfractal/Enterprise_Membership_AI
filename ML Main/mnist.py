from sklearn.datasets import fetch_openml

mnist = fetch_openml('mnist_784', version=1, as_frame=False, parser='auto')
mnist.keys()

#Call data and target
#image data format 28 x 28 = 784

X = mnist['data']
y= mnist['target']

print("X: ", X.shape)
print("y: ", y.shape)