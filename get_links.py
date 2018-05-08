from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_links(url,filter):
    page = urlopen(url)
    soup = BeautifulSoup(page,'html.parser')
    links = soup.find_all('a')
    result = []
    for link in links:
        temp = link.get('href')
        if filter in temp:
            result.append(temp)
    return result
    