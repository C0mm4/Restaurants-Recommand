import numpy as np
import pandas as pd
from datetime import datetime
import sql

# 노드 클래스
class Node:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    pass

# 장소 클래스 (노드)
class Place(Node):
    def __init__(self, name, index):
        self.name = index
        self.value = name
    def __str__(self):
        return str(self.name)

# 키워드 클래스 (노드)
class Keyword(Node):
    def __init__(self, name):
        self.name = name

# 엣지 클래스
class Edge:
    def __init__(self, start, target, weight):
        self.start = start
        self.target = target
        self.weight = weight

    def __str__(self):
        return self.start + self.target + self.weight
    pass

# 그래프 클래스
class Graph:
    # 그래프 내에서 사용될 노드와 엣지 딕셔너리 선언
    nodes = dict()
    edges = dict()
    def __init__(self):
        print("Create Graph")
        datas = pd.read_csv("testedgelists.csv")
        for row in range(1, len(datas)):
            self.addEdge(datas['name'][row], datas['index'][row], datas['nouns'][row], datas['Probability'][row])
    
    # name 이름을 가지는 노드 가져옴 (Place는 Index)
    def getNode(self, name):
        ret = self.nodes.get(name, None)
        return ret

    def getEdge(self, start, target):
        ret = self.edges.get((start, target), None)
        return ret

    def addPlaceNode(self, name, start):
        if self.getNode(start) == None:
            node = Place(name, start)
            self.nodes[start] = node

    def addKeywordNode(self, name):
        if self.getNode(name) == None:
            node = Keyword(name)
            self.nodes[name] = node

    def addEdge(self, name, start, target, weight = 1):
        if self.getEdge(start, target) == None:
            if self.getNode(start) == None:
                self.addPlaceNode(name ,start)
            if self.getNode(target) == None:
                self.addKeywordNode(target)

            edge = Edge(self.nodes[start], self.nodes[target], weight)
            self.edges[self.nodes[start], self.nodes[target]] = edge
            
    def showNodes(self):
        for i in self.nodes:
            print(i)

    def showEdges(self):
        for k,v in self.edges:
            print(self.getEdge(k,v).start)

    def getEdgesatNodeName(self, start):
        ret = []
        startnode = self.nodes[start]
        for k, v in self.edges:
            if k == startnode or v == startnode:
                ret.append(self.getEdge(k,v))
        return ret

    def DFS(self, start):
        stack = []
        for s in start:
            startnode = self.nodes.get(s, None)
            if startnode != None:
                stack.append((startnode, 1))
        tmp = []
        ret = []
        search = dict()

        while stack:
            n = stack.pop()
            if search.get(n[0], True):
                search[n[0]] = False
                if(n[1] <= 0.7):
                    continue
                edgelist = self.getEdgesatNodeName(n[0].name)
                if isinstance(n[0], Place):
                    
                    tmp.append((n[0].name, n[1]))
                for edge in edgelist:
                    if isinstance(n[0], Place):
                        stack.append((edge.target, n[1] * edge.weight))
                    else:
                        stack.append((edge.start, n[1] * edge.weight))
                
        
        tmp.sort(key = lambda x:x[1], reverse=True)
        for tp in tmp:
            ret.append(tp[0])
        return ret

    def search(self, start, cur, search, table, wherea):
        result = self.DFS(start)
        ret = sql.select(cur, search, table, result, wherea)

        return ret

t = datetime.now()
g = Graph()
ct = datetime.now()

diff = ct - t
print(diff.seconds)
t = ct

placelist = g.DFS(['만족', '짬뽕'])
ct = datetime.now()
diff = ct - t
print(diff.seconds)
t = ct


con = sql.connect('localhost', 'test', 'test', 'restaurants')
cur = con.cursor()

ret = sql.select(cur, '*', 'restaurant', wherei = placelist, wherea = '강남')

for re in ret:
    print(re)