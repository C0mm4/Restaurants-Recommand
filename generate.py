import csv
import random as rand
import pandas as pd

f = open("User_file.csv", 'w', newline = '')
wr = csv.writer(f)

class User():
  age = int()
  gender = int()
  time = int()
  price = int()

class Food():
  type = int()
  price = int()
  review = float()
  pass

class Order():
  user = User()
  food = Food()
#  fd = pd.read_csv("Food Data.csv", header=None)

  def selectFood(self):
    index = rand.randrange(0,151)
    print(self.fd[[index]])



def generateUser(x):
  index = x
  age = rand.randrange(20,70)
  gender = rand.randrange(0,2)
  wr.writerow([index, age, gender])
  pass


wr.writerow(["Index", "Age", "Gender"])
for x in range(100000):
  if(x % 10000 == 0):
    print(x, " datas generate.")

  generateUser(x)


'''
ord = Order()
ord.selectFood()
'''