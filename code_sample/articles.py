from selenium import webdriver
from bs4 import BeautifulSoup
import time
import undetected_chromedriver as uc
import random
from selenium.webdriver.chrome.service import Service

service = Service('.\chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--auto-open-devtools-for-tabs")
driver = uc.Chrome(service=service, options=options)

with open('issues.txt', 'r', encoding='utf-8') as f:
    issue_links = f.read().split(' ')

url1 = '#'
art_links = []
for i in issue_links:
    url = url1 + i
    driver.get(url)
    page = driver.page_source
    time.sleep(random.uniform(3, 5))
    soup = BeautifulSoup(page, 'html.parser')
    for link in soup.find_all('a', {"class": "issueContentsArticleLink linkHoverDark d-inline-block"}):
        if link.get('href') not in art_links:
            art_links.append(link.get('href'))
    time.sleep(random.uniform(2, 5))

with open('articles.txt', 'w', encoding='utf-8') as f:
    f.write(' '.join(art_links))
