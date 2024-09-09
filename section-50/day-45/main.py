from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
articles = soup.find_all("h3", class_="title")
# article_links = []
# article_texts = []
# for tag in articles:
#     text = tag.getText()
#     article_texts.append(text)
#     link = tag.find(name="a").get("href")
#     article_links.append(link)

article_upvote = [score.getText() for score in articles]

# print(article_texts[index_num])
# print(article_links[index_num])
movies = article_upvote[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")

# response = requests.get("https://news.ycombinator.com/news")
# yc_web_page = response.text

# soup = BeautifulSoup(yc_web_page, "html.parser")
# articles = soup.find_all("span", class_="titleline")
# article_links = []
# article_texts = []
# for tag in articles:
#     text = tag.getText()
#     article_texts.append(text)
#     link = tag.find(name="a").get("href")
#     article_links.append(link)

# article_upvote = [int(score.getText().split()[0]) for score in soup.find_all("span", class_="score")]

# largest_num = max(article_upvote)
# index_num = article_upvote.index(largest_num)

# print(article_texts[index_num])
# print(article_links[index_num])
# print(article_upvote[index_num])



# # import lxml


# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.string)
# # print(soup.prettify())
# # all_anchor_tags = soup.find_all(name="a")

# # for tag in all_anchor_tags:
# #     # print(tag.getText())
# #     print(tag.get("href"))

# # heading = soup.find(name="h1", id="name")
# # print(heading)

# # company_url = soup.select_one(selector="p a")
# # print(company_url)

# # company_url = soup.select_one("#name")
# # print(company_url)

# headings = soup.select(".heading")
# print(headings)