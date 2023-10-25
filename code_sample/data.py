from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time
import random
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service

service = Service('.\chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = uc.Chrome(service=service, options=options)
driver.maximize_window()

with open('articles.txt', 'r', encoding='utf-8') as f:
    art_links = f.read().split(' ')

w_file = open("#.csv", mode="w", encoding='utf-8')
file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
file_writer.writerow(["doi", "author", "title", "year", "abstract", "journal"])

url1 = '#'
for i in art_links:
    url = url1 + i
    time.sleep(random.uniform(3, 5))
    driver.get(url)
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')

    doi = authors = abstract = data = title = ''
    if soup.find('meta', {"property": "og:title"}):
        title = str(soup.find('meta', {"property": "og:title"})["content"]).strip()
    authors1 = []
    for m in soup.find_all('meta', {"property": "article:author"}):
        authors1.append(str(m["content"]).strip())
        authors = '; '.join(authors1)
    if soup.find('meta', {"name": "citation_doi"}):
        doi = str(soup.find('meta', {"name": "citation_doi"})["content"]).strip()
    if soup.find('meta', {"property": "og:description"}):
        abstract = str(soup.find('meta', {"property": "og:description"})["content"]).strip()
    if soup.find('meta', {"property": "article:published_time"}):
        data = str(soup.find('meta', {"property": "article:published_time"})["content"]).strip()[:4]
    journal = '#'
    file_writer.writerow([doi, authors, title, data, abstract, journal])
    doi = authors = abstract = data = title = ''
    time.sleep(random.uniform(2, 6))
