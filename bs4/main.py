from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_pages = response.text
soup = BeautifulSoup(yc_web_pages, "html.parser")
article_title = soup.find_all(name="a", class_="storylink")
article_point = soup.find_all(name="span", class_="score")
# for x in article_title:
#     print(x.get("href"))
title = []
title_link = []
for x in article_title:
    title.append(x.string)
    title_link.append(x.get("href"))
point = [int(x.text.split()[0]) for x in soup.find_all(name="span", class_="score")]

print(title)
print(title_link)
max_point = point.index(max(point))

print(f"""
article" is {title_link[max_point]}
link :{title_link[max_point]}
point is {point[max_point]}""")
