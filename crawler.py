import requests
from bs4 import BeautifulSoup

# fetch the page
URL = "https://encore.securecafe.com/onlineleasing/encore-at-forest-park/rentaloptions.aspx?MoveInDate=8/1/2022"
page = requests.get(URL)

# parse to soup with beautiful soup
soup = BeautifulSoup(page.content, "html.parser")

# select element by selector
# divFPH_2322187 -> the table for FloorPlanID=2322187, i.e. A1
# TODO: it's a dynamic site, find a better tutorial
results = soup.find(id="divFPH_2322187")
print(results.prettify())