import requests
from bs4 import BeautifulSoup

'''Scrapes the top 250 movies from IMDB's list at https://www.imdb.com/chart/top/ and outputs the top 20 in the list with the title and IMDB rating'''

url = "https://www.imdb.com/chart/top"
page = requests.get(url)
count = 0

soup = BeautifulSoup(page.content, "lxml")

movies_list = soup.find(class_="lister-list")
title = movies_list.find_all(class_="titleColumn")
rating = movies_list.find_all(class_="ratingColumn imdbRating")

for movie, rating in zip(title[:20], rating[:20]):
    count += 1
    print(f'{count}\n{movie.find("a").contents[0]} {movie.find("span").contents[0]} \nIMDB rating: {rating.find("strong").contents[0]}\n')