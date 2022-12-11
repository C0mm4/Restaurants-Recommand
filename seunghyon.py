import pandas as pd
import os
from urllib import request

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


def getPrice(string):
  price = 0
  for s in string:
    if s == ',' or s == '￦':
      continue
    price *= 10
    price += int(s)

  return price

options = webdriver.ChromeOptions()
options.add_argument('window-size=1920,1080')

driver = webdriver.Chrome('chromedriver', options=options)
driver.implicitly_wait(5)

driver.get(url='https://insainnebike.com/INSAINNE.php')

products=[]
specifics = ['Product Name', 'Product Price', '프레임', '앞포크', '핸들바', '핸들스템', '브레이크레버', '시프트레버', '브레이크', '앞변속기', '뒷변속기', '크랭크', '스프라켓', '체인' '휠세트', '타이어', '시트포스트', '안장', '무게']

# 제품 리스트 버튼
button = driver.find_element(By.XPATH, "//nav[@class='navigation-shop']//ul[@class='navigation']//li//a")
button.click()

button = driver.find_element(By.XPATH, "//nav[@class='navigation-shop']//ul[@class='navigation']//li//div[@class='navigation-flyout']//ul//li//a")
button.click()

items = driver.find_elements(By.XPATH, "//article//figure//span[@class = 'align-bottom']")
itemcount = len(items)

for i in range(itemcount):
  product=[]
  item = driver.find_elements(By.XPATH, "//article//figure//figcaption//div//div//a[@class = 'link link_fff_red2']")[i]
  item.send_keys(Keys.ENTER)

  # 제품명 따옴
  productname = driver.find_element(By.XPATH, "//section//article//section//div//div//h2[@class='color3 fw4']").text
  product.append(productname)

  if "2018" in productname:
    driver.back()
    continue

  print(productname)


  price = driver.find_element(By.XPATH, "//div//div//div//div//font[@style = 'color:#999']").text
  # price = getPrice(price)
  product.append(price)


  img_url = driver.find_element(By.XPATH, "//a[@class='MagicZoom']").get_attribute('href')
  request.urlretrieve(img_url, 'img/insa/'+productname+'.jpg')

  about = driver.find_elements(By.XPATH, "//div[@class = 'col-sm-12']//ul/li")


  print(product)
  products.append(product)
  driver.back()

print(products[0])

print("Start generate DataFrame")
data = pd.DataFrame(products, columns = specifics)
data.set_index('Product Name', inplace=True)
print("Saved csv file")
data.to_csv("test.csv", encoding = 'utf-8-sig')
print("Finish Him")
driver.close()