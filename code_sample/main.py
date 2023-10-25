from selenium import webdriver
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service

service = Service('.\chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = uc.Chrome(service=service, options=options)
driver.maximize_window()

url = '#'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
}

driver.get(url)
page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')

issue_links = []
for link in soup.find_all('a'):
    if link.get('href') and "issue" in link.get('href') and link.get('href') not in issue_links:
        issue_links.append(link.get('href'))
with open('issues.txt', 'w', encoding='utf-8') as f:
    f.write(' '.join(issue_links))
