import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 1)
fx = x ** 2

plt.plot(x, fx)
plt.show()

x_new = 10
derivative = []
y = []
learng_rate= 0.1
for i in range(100):
	old_value = x_new
	derivative.append(old_value - learng_rate * 2 * 
	old_value)
	x_new = old_value - learng_rate *2* old_value
	y.append(x_new ** 2)
plt.plot(x, fx)
plt.scatter(derivative, y)
plt.show()