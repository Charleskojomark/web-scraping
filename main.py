from bs4 import BeautifulSoup
import requests
response = requests.get("https://news.ycombinator.com")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
article= soup.find_all(name="span", class_ = "titleline")
article_texts = []
article_links = []
for a in article:
    article_tag = a.find(name="a")
    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.get("href")
    article_links.append(article_link)
    

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
largest_number = max(article_upvotes)
largest_number_index = article_upvotes.index(largest_number)
print(article_texts[largest_number_index])
print(article_links[largest_number_index])
print(article_upvotes[largest_number_index])