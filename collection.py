from bs4 import BeautifulSoup
import requests
import pandas as pd

# Business
url = "https://news.google.com/u/1/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx6TVdZU0JXVnVMVWRDR2dKT1FTZ0FQAQ?hl=en-NA&gl=NA&ceid=NA%3Aen"

l = []
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
for href in soup.find_all("a", class_ = "DY5T1d RZIKme"):
  l.append(href.contents[0])

# Technology
url = "https://news.google.com/u/1/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGRqTVhZU0JXVnVMVWRDR2dKT1FTZ0FQAQ?hl=en-NA&gl=NA&ceid=NA%3Aen"

ll = []
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
for href in soup.find_all("a", class_ = "DY5T1d RZIKme"):
  ll.append(href.contents[0])

# Sports
url = "https://news.google.com/u/1/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp1ZEdvU0JXVnVMVWRDR2dKT1FTZ0FQAQ?hl=en-NA&gl=NA&ceid=NA%3Aen"

lll = []
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
for href in soup.find_all("a", class_ = "DY5T1d RZIKme"):
  lll.append(href.contents[0])


dic1 = {"title": l, "label": "business"}
df1 = pd.DataFrame(dic1)
dic2 = {'title': ll, 'label': 'technology'}
df2 = pd.DataFrame(dic2)
dic3 = {'title': lll, 'label': 'sports'}
df3 = pd.DataFrame(dic3)

final = pd.concat([df1, df2, df3])

final.to_csv("./train_data.csv", index=False)
