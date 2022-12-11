import pandas as pd
import numpy as np
from multiprocessing import Process,Queue

from datetime import datetime

import os

def big_table_save(num, table):
    table.to_csv("test"+str(num)+"proc.csv",index=False,header=None)
    print(num, "process success")

def total_table_save(table):
    counting = len(table)
    if counting <= 100000:
        big_table_save(0,table)
    else:
        procs = []
        numbers=list(range(0,10))
        quotient, remainder = (counting//10, counting%10)
        for index, number in enumerate(numbers):
            if number!=9:
                part_table=table[quotient*number:quotient*(number+1)]
            else:
                part_table=table[quotient*number:]
            proc = Process(target=big_table_save, args=( number, part_table  )) 
            procs.append(proc) 
            proc.start()   
        for proc in procs: 
            proc.join()
t = datetime.now()

data = pd.read_csv("edgelists.csv", encoding = 'utf-8-sig')

edges = dict()

for row in range(len(data)):
  print(data['index'][row])
  target = data['nouns'][row]
  if target in edges:
    value = edges[target]
    value.append((data['index'][row],data['Probability'][row]))

  else:
    value = [(data['index'][row], data['Probability'][row])]

  edges[target] = value

print((datetime.now() - t).seconds)
t = datetime.now()
df = pd.DataFrame.from_dict(edges, orient='index')


print((datetime.now() - t).seconds)
t = datetime.now()

total_table_save(df)

