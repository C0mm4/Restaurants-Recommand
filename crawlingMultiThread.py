import pandas as pd
import numpy as np

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from threading import Thread

from time import sleep

data = pd.read_csv("combined.csv")
urls = data['place url']
names = data['place name']

placereviews = []

start = 30000
slicing = 100
end = min(start+slicing, len(urls))

cnt = 0

tdCnt = 10
tds = []

class crawTd(Thread):
  def __init__(self, start, end, tdindex):
    super().__init__()
    self.options = webdriver.ChromeOptions()
    self.options.add_argument('window-size=1920,1080')


    self.cnt = 0
    self.placereviews = []
    self.startpoint = start
    self.end = end
    self.tdindex = tdindex


  def run(self):    
    self.driver = webdriver.Chrome('chromedriver', options=self.options)
    self.driver.implicitly_wait(5)
    for index in range(self.startpoint, self.end):
      self.cnt += 1
      print(self.cnt/slicing * tdCnt * 100 , '% processed.')
      print('now processed index number ', index)
      self.driver.get(url = urls[index])
      self.place = []
      try:
        reviewcount = self.driver.find_element(By.XPATH, "//div//div//a//span[@class='color_g']").text
      except:
        continue
      reviewcount = int(reviewcount.strip('()'))
      print(urls[index])

      if reviewcount == 0:
        continue
      self.placename = names[index]
      try:
        self.score = self.driver.find_element(By.XPATH, "//div//em[@class='num_rate']")
      except:
        continue

  

      self.place.append(index)
      self.place.append(self.placename)
      self.place.append(self.score)
      print(self.placename)

      if reviewcount > 3 :
        try:
          morebutton = self.driver.find_element(By.XPATH, "//div//div//div//div//a[@class='link_more']")
          if morebutton.text == "메뉴 더보기":
            morebutton = self.driver.find_elements(By.XPATH, "//div//div//div//div//a[@class='link_more']")[1]
          while(morebutton.text == "후기 더보기"):
            morebutton.click()
            sleep(0.3)
        except:
          pass


      reviewerNames = self.driver.find_elements(By.XPATH, "//div[@class='unit_info']//a")
      reviewScores = self.driver.find_elements(By.XPATH, "//div[@class='star_info']//div//span[@class='ico_star star_rate']//span")
      reviewerAvg = self.driver.find_elements(By.XPATH, "//div[@class='unit_info']//span[@class='txt_desc']")
      reviercmts = self.driver.find_elements(By.XPATH, "//div[@class='comment_info']")


      for rev in range(min(len(reviewerNames),len(reviewScores), len(reviewerAvg), len(reviercmts))):
        self.review = []
        self.review.append(index)
        self.review.append(self.placename)
        self.review.append(reviewerNames[rev].text)
        reviewScore = reviewScores[rev].get_attribute('style')
        reviewScore = reviewScore[-5:]
        print(reviewScore)
    
        if reviewScore[0] ==':':
          reviewScore = int(reviewScore[1:3])
        else:
          reviewScore = int(reviewScore[0:3])
        reviewScore /= 20
    
        self.review.append(reviewScore)


        self.review.append(reviewerAvg[rev*2+1].text)
        cmd = reviercmts[rev].text
        slicindex = 0
        if len(cmd):
          for textindex in range(len(cmd)-1, 0, -1):
            if cmd[textindex] == '좋':
              slicindex = textindex
              break
    
        cmd = cmd[:slicindex]

        self.review.append(cmd.replace("더보기", ""))

        print(cmd)
        self.placereviews.append(self.review)
      
    self.npreviews = np.array(self.placereviews)
    self.df = pd.DataFrame(self.npreviews, columns = ['index', 'place name', 'reviewer', 'score', 'useravg', 'comment'])
    self.df.to_csv("Tdreview" + str(self.tdindex)+ '.csv', encoding = 'utf-8-sig')


for td in range(tdCnt):
  tdstep = int(slicing / tdCnt)
  tdstart = start + td * tdstep
  tdend = tdstart + tdstep
  tds.append(crawTd(tdstart, tdend, td))
  
for td in tds:
  td.start()
  td.join()