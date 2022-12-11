import graph
import pandas as pd

G = graph.Graph()

datas = pd.read_csv('test.csv', encoding='utf-8-sig')

for row in range(1,len(datas)):
  G.addEdge(row['place'])