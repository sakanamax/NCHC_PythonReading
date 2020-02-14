# Edit by Max 2020/2/14
from selenium import webdriver


#web = webdriver.Chrome(r"/home/sakana/Dropbox/Max/Learn/python/NCHC_PythonReading/todo/sakana/Python程式設計實務-第2版/Exercise/chromedriver")
# 書上說 r 是為了不要解譯這個字串, 但是發現不加上 r , 在 linux 底下好像也可以用
web = webdriver.Chrome("/home/sakana/Dropbox/Max/Learn/python/NCHC_PythonReading/todo/sakana/Python程式設計實務-第2版/Exercise/chromedriver")
# 測試相對路徑也可以, 只要找的到
web = webdriver.Chrome("./chromedriver")

web.get('https://facebook.com')
web.close()
