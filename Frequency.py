import pandas as pd
import re
from konlpy.tag import Kkma
from collections import Counter
import numpy as np

data = pd.read_csv('allreviews.csv', encoding = 'utf-8-sig')
placeScores = []
datacomment = data['comment']
dataplace = data['place name']
dataScore = data['score']
placeList = []
placeIndexList = []
placeReviewCounts = []
countList = []
count = Counter()
kkma = Kkma()
prePlace = dataplace[1]

allcount = dataplace.shape[0]

def sigmoid(x, cnt = 0):
  return 1 / (1 + np.exp(-x + cnt))

# 리뷰 코멘트를 명사로 분석 후 개수를 셈

print("Start Analystic Nouns.")
cnt = 0
sumscore = 0
for index in range(allcount):
  if prePlace != dataplace[index]:
    countList.append(count)
    placeIndexList.append(data['index'][index])

    placeList.append(prePlace)
    prePlace = dataplace[index]
    placeScores.append(sumscore/cnt)
    placeReviewCounts.append(cnt)
    cnt = 0
    sumscore =0
    count = Counter()
  cnt += 1
  sumscore += dataScore[index]

  if index % 1000 == 0:
    print(index/allcount * 100, "% processed.")

  try:
    comment = datacomment[index]
    tmp = Counter(kkma.nouns(comment))
  except:
    continue

  count = count + tmp
  
print("100 % processed.")


# 리스트 첫 객체로 공백 들어가기에 팝, 마지막 객체 어펜드
print(sumscore, cnt)
countList.append(count)
placeIndexList.append(data['index'][allcount-1])
placeList.append(dataplace[allcount-1])
placeScores.append(sumscore/cnt)
placeReviewCounts.append(cnt)

# 각 Counter에서 최대빈도수를 가지는 20개를 추림

mostList = []

print("Start Find Most Comment")
for i in countList:
  mostList.append(i.most_common(20))

# 각 단어의 빈도 확률을 추정하기 위해 단어 수를 카운트함

sumList = []
nouncntList = []
print("Count every nouns")
for most in mostList:
  sum = 0
  nouncnt = []
  for m in most:
    nouncnt.append(m[1])
    sum += m[1]
  sumList.append(sum)
  nouncnt = np.array(nouncnt)
  nouncntList.append(nouncnt)


# 각 단어들을 확률화 함

perList = []
print("Start processed weight")
for most in range(len(mostList)):
  percent = []
  mean = nouncntList[most].mean()
  std = nouncntList[most].std()
  if std != 0:
    for m in mostList[most]:
      p = (m[1] - mean) / std
      percent.append(p)
  else:
    for m in mostList[most]:
      p = m[1] - mean
      percent.append(p)
    
  cnt = placeReviewCounts[most]
  cnt = sigmoid(cnt, 0)
  cnt = sigmoid(cnt, 0)
  percent = np.array(percent)
  percent = sigmoid(percent,cnt)
  percent = percent * placeScores[most] / 5

  perList.append(percent)

# 각 단어들의 확률을 토대로 노드 리스트를 만듦

nodeList = []

placeCount = len(placeList)

print("Start Makes Edges")

for place in range(placeCount):
  placeName = placeList[place]
  placeindex = placeIndexList[place]
  for most in range(len(mostList[place])):
    compo = [placeindex, placeName, mostList[place][most][0], perList[place][most]]
    nodeList.append(compo)
  print("{0} % processed.".format(place / placeCount * 100))
print("100 % processed.")
nparr = np.array(nodeList)
df = pd.DataFrame(nodeList, columns = ['place index ', 'place name', 'nouns', 'Probability'])
df.to_csv('testcountedgelist.csv',encoding = 'utf-8-sig')