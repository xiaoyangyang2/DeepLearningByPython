

#4.3 数值微分
import matplotlib.pylab as plt
import numpy as np

#4.3.1 用中心差分实现数值微分
def numerical_diff(f, x):
	h = 1e-4 #0.0001
	return (f(x+h) - f(x-h) / 2*h)


#4.3.2 数值微分的例子
def function_1(x):
	return 0.01*x**2 + 0.1*x

x = np.arange(0.0, 20.0, 0.1) #以0.1为间隔，从0到20
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x, y)
plt.show()

