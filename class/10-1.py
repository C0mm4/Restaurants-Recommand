import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [1,2,3,4,5]
y = [11,2,13,4,5]

y1 = [5,9,3,11,4]

'''
plt.plot(x,y, 'bo', label = "Sold")  	# b = blue o = circle s = square
plt.plot(x,y1, label="On Shelves")		# firstletter = collor secondletter = shape

plt.legend(loc="upper left")
plt.title("test plot")
plt.xlabel("daily")
plt.ylabel("No.39 Utopia")
plt.axis([0,6,0,30])
plt.savefig("fig1.pdf")

plt.show()


p = np.array([[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]])
p1 = np.array([2.5,1])
plt.plot (p[:,0], p[:,1], 'rs')
plt.plot(p1[0], p1[1], 'go')
plt.show()




x = np.linspace(0, 5, 10)
y = x**2

plt.plot(x,y,'bo-', linewidth=3, markersize = 10)			# - = line

plt.show()


x = np.logspace(0,2, 1000)
y = x ** 2
y1 = x ** 1.5
y2 = x ** 0.5

plt.plot(x,y,'bo-', label = "x ^ 2 = y")
plt.plot(x,y1,'ro-', label = "x ^ 1.5 = y")
plt.plot(x,y2, 'go-', label = 'x ^ 0.5 = y')

plt.legend(loc = "upper left")
plt.title("X Y")
plt.xlabel("x")
plt.ylabel("y")

plt.show()


x = np.random.standard_normal(size=1000)

plt.hist(x)
plt.show()


x = np.random.rand(30)
y = np.random.rand(30)
color = np.random.rand(30)
plt.scatter(x,y,c=color, marker='*', alpha=0.7)
#plt.hist(x)
plt.show()


x = pd.Series([7,3,5,1], index=['dnjf','ghk','tn','ahr'])
y = pd.Series([7,9,2,4], index = ['dnjf', 'ahr', 'xh', 'dlf'])
print(x)
print(x[['ghk','ahr']])
print(x.index)
print(x.values)
print(sorted(x.values))

print(x+y)


test = [1,3,2,5,2,1]
x = pd.Series(test)
print(pd.unique(x))
'''

test = {'Hong':25, 'Park':21, 'Kim':27}
x = pd.Series(test.keys, test.values)
print(x)
print(x['Hong'])

# data.go.kr