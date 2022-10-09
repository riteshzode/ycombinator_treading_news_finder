import pandas as pd
from bs4 import BeautifulSoup
import requests

page_no = []
news_title = []
news_link = []
news_score = []

page = 0
for i in range(1, 6):
    # Finding the top 5 important news of 5 pages in ycombinator website

    r = requests.get(url=f"https://news.ycombinator.com/news?p={i}")

    soup = BeautifulSoup(r.text, 'html.parser')

    # print(soup.prettify())

    text = [i.get_text() for i in soup.find_all(name="span", class_="titleline")]
    link = [i.a["href"] for i in soup.find_all(name="span", class_="titleline")]
    score = [int(i.get_text().split()[0]) for i in soup.find_all(name="span", class_="score")]

    index = score.index(max(score))

    page += 1
    print(f"Page : {page}")
    print(f"No : {index + 1}")
    print(f"Title : {text[index]}")
    print(f"points : {score[index]}")
    print(f"Link : {link[index]}")

    page_no.append(page)
    news_title.append(text[index])
    news_link.append(link[index])
    news_score.append(score[index])

dict = {"Page Number": page_no, "News Title": news_title, "News Link": news_link, "News Score": news_score}

df = pd.DataFrame(dict)

df.to_csv("news.csv", index=False)

print("File Created")