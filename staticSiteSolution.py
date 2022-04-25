# STATIC SITE SOLUTION
# # fetch the page
# page = requests.get(URL)

# # parse to soup with beautiful soup
# soup = BeautifulSoup(page.content, "html.parser")

# # select element by selector
# # divFPH_2322187 -> the table for FloorPlanID=2322187, i.e. A1
# # TODO: it's a dynamic site, find a better tutorial
# # results = soup.find(id="divFPH_2322187")
# results = soup.find(id="RentCafeContent")
# print(results.prettify())