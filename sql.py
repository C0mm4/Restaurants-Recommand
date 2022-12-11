import pymysql
import pandas as pd



# Save DB Data
'''
data = pd.read_csv('combined.csv', encoding = 'utf-8-sig')

for row in range(len(data)):
  if "'" in data['name'][row]:
    name = data['name'][row].replace("'", " ")
  else:
    name = data['name'][row]
  sql = "INSERT INTO restaurant(placeindex, placename, adress, placex, placey)\nvalue(" 
  sql += str(data['index'][row]) + ", '"  + name + "', '" + data['adress'][row]
  sql += "'," + str(data['x'][row]) + "," + str(data['y'][row]) + ");"
  print(sql)
  cur.execute(sql)

con.commit()

con.close()
'''

def connect(host, user, password, db):
  con = pymysql.connect(host = host, user = user, password = password, db = db,
  charset = "utf8")

  return con

def select(c, select, table, wherei = None, wherea = None):
  if wherei == None and wherea == None:
    sql = "select {0} from {1};".format(select, table)
  if wherei == None and wherea != None:
    sql = "select {0} from {1} where adress like '%{2}%'".format(select, table, wherea)
  else:
    if len(wherei) == 1:
      sql = "select {0} from {1} where placeindex = '{2}'".format(select, table, wherei)
      if wherea == None:
        sql += ';'
      else:
        sql += "and adress like '%{0}%';".format(wherea)
        
    else:
      sql = "select {0} from {1} where placeindex in {2}".format(select, table, tuple(wherei))
      if wherea == None:
        sql += ';'
      else:
        sql += "and adress like '%{0}%';".format(wherea)
      
  print(sql)
  c.execute(sql)

  ret = c.fetchall()
  return ret