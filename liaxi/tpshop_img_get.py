import time
from numpy import random

from selenium import webdriver
import urllib.request

# 实例化一个浏览器对象
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://localhost")
js = 'window.scrollTo(0, 2000)'
driver.execute_script(js)


list_a = []
img_name = 0

texts = driver.find_elements_by_xpath("//img")
for i in texts:
    url_png = i.get_attribute("src")
    if url_png not in list_a:
        list_a.append(url_png)
time.sleep(2)
print(list_a)
print(len(list_a))
for url_png in list_a:
    req = urllib.request.urlopen(url_png)
    img_content = req.read()
    with open("./img/{}.jpg".format(img_name), "wb") as f:
        f.write(img_content)
    img_name += 1

driver.quit()