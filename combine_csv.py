import numpy as np
import pandas as pd
import os
import collections

dir_path = '.\\reviews'

filename = []

for (root, directories, files) in os.walk(dir_path):
  for d in directories:
    d_path = os.path.join(root, d)

  for file in files:
    file_path = os.path.join(root, file)
    filename.append(file_path)


combine_file = pd.concat([pd.read_csv(f, encoding = 'utf-8-sig') for f in filename])

#results = list(map(dict, collections.OrderedDict.fromkeys(tuple(sorted(d.items())) for d in combine_file)))
combine_file.to_csv("csvs.csv", encoding='utf-8-sig')