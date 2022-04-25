import requests
from bs4 import BeautifulSoup
from selenium import webdriver
# from webdriver_manager.chrome import GeckoDriverManager

# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

# use selenium to fetch dynamic content
URL = "https://encore.securecafe.com/onlineleasing/encore-at-forest-park/rentaloptions.aspx?MoveInDate=8/1/2022"

options = webdriver.ChromeOptions()
options.add_argument("--enable-javascript")

driver = webdriver.Chrome('./chromedriver.exe',chrome_options=options)
driver.get(URL)

# parse to soup with beautiful soup
html = driver.page_source
soup = BeautifulSoup(html,features="html.parser")

# prints out the whole thing, test purpose
print(soup.get_text())

# check out the docs for the kinds of things you can do with 'find_all'
# this (untested) snippet should find tags with a specific class ID
# see: http://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-by-css-class
res = soup.findall()
print(res.prettify())