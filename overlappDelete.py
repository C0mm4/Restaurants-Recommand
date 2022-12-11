import pandas as pd
import numpy as np
import collections

datas = pd.read_csv("allreviews.csv", encoding='utf-8-sig')


df = pd.DataFrame(np.array(datas))

duplicant = datas.duplicated(['index', 'comment'])

for b in range(len(duplicant)):
    if duplicant[b]:
        datas.drop(b, inplace = True)


print(datas.head(5))

datas.to_csv('testduplicant.csv', encoding='utf-8-sig')