import pandas as pd
import numpy as np
from numpy import NAN
'''
data = { 'age' : [34, 37, 43, 12],
				'name' : ['Kill', 'Min', 'Seo', 'Tou'],
        'height' : [177, 177, 169, 182],
}

x =  pd.DataFrame(data, columns = ['name', 'age', 'height'])
print (x)
		# head()  tail() default  = 5

print(x.iloc[2])
		# iloc = index slice


a = [[1,2], [3,4], [5,6], [7,8], [9,10]]
data = pd.DataFrame(a, columns = ['SuOn','SangOn'])
data['SuOn'] = data['SuOn'].astype('float')

print(data)


data = pd.DataFrame(np.arange(12).reshape(3,4), columns = ['A','B','C','D'])
data.D[2] = 'NaN'
print(data)
data.drop(['D'], axis = 1)
print(data)


data = {'MaxSpeed' : [24, 36, 43, 27],
			'Price' : [21600, NAN, 43000, NAN],
}

x = pd.DataFrame(data)
x = x.dropna(subset=['Price'], axis=0) # inplace : change Origin data
avg = x['price'].mean()
print(x.replace(NaN, avg))
print(x)


price = np.random.randint(100, size=8) * 10000
data = pd.DataFrame(price, columns = ['Price'])
group_name = ['Low', 'Middle', 'High']
data['Level'], x = pd.cut(data['Price'], 3, labels = group_name, retbins=True)


print(data)
'''

data = pd.read_csv('test.csv', encoding='utf-8')
# How to read variable encode type?

