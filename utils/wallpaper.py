import requests
from bs4 import BeautifulSoup
import random

def img(name):


    i = random.randint(0,143)
    link = f'https://www.peakpx.com/en/search?q={name}&page={i}'
    data = requests.get(link)

    soup = BeautifulSoup(data.text, 'html.parser')

    # print(soup.prettify)

    figure_tags = soup.find_all("figure")


    links = []
    for figure_tag in figure_tags:
        figure_links = figure_tag.find_all("link") 
        for link in figure_links:
            href = link.get("href")
            if href:
                links.append(href)


    return links
