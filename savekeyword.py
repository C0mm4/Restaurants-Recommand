import pandas as pd
import numpy as np
from datetime import datetime

t = datetime.now()

data = pd.read_csv("testedgelists.csv", encoding = 'utf-8-sig')

edges = dict()
print(data.head(10))
for row in range(len(data)):
  print(data['index'][row])
  target = data['nouns'][row]
  if target not in edges:
    edges[target] = ''

print((datetime.now() - t).seconds)
t = datetime.now()
df = pd.DataFrame.from_dict(edges, orient='index')


print((datetime.now() - t).seconds)
t = datetime.now()

df.to_csv('keywords.csv', encoding = 'utf-8-sig')

print((datetime.now() - t).seconds)