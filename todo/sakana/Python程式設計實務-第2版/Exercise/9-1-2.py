from urllib.parse import urlparse
uc = urlparse('https://tw.stock.yahoo.com/news_list/url/d/e/N1.html?q=&pg=4')
print("uc =", uc)
print("uc.netloc =", uc.netloc)
print("uc.path =",uc.path)
print("uc.query =", uc.query)