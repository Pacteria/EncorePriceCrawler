from math import floor
from attr import attr
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv
from datetime import date

absPATH = 'E:/Github_repos/EncorePriceCrawler/'

def crawler_Encore():
    '''
    parse pricing information from encore's website
    returns a python list of pricing info
    '''
    URL = "https://encore.securecafe.com/onlineleasing/encore-at-forest-park/rentaloptions.aspx?MoveInDate=7/1/2022"

    # use selenium to fetch dynamic content
    options = webdriver.ChromeOptions()
    options.add_argument("--enable-javascript")
    options.add_argument('headless')# this runs the task without opening a browser window

    driver = webdriver.Chrome(absPATH+'chromedriver.exe',options=options)
    driver.get(URL)

    # prevents driver shutting itself down
    time.sleep(1)

    # parse to soup with beautiful soup
    html = driver.page_source
    soup = BeautifulSoup(html,features="html.parser")

    # TODO:THIS IS NOT A COMPREHENSIVE MAPPING! THERE ARE OTHER FLOOR PLANS!
    floorPlanIdMap = {
            'divFPH_2322187':'A1 - 1b1b',
            'divFPH_2322190':'A3 - 1b1b',
            'divFPH_2322194':'B2 - 2b2b',
            'divFPH_2322196':'B2B - 2b2b',
            'divFPH_2322197':'B3 - 2b2b',
            'divFPH_2322198':'C1 - 3b2b',
            'divFPH_2322186':'S1 - studio',
    }

    # parse all table, no specific floor plan
    data = []
    allTables = soup.find_all('table')
    for table in allTables:
        if "ui-datepicker-calendar" in table.get('class'): # there's a calender table that we don't need
            continue
        table_id = table.get('id')
        table_body = table.find('tbody')
        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele]+([floorPlanIdMap[table_id]])) # Get rid of empty values

    # write result to csv file
    PATH = absPATH+f'pricingHistory/encore/{date.today()}.csv'
    fields = ['UnitID', 'Sq.Ft.', 'Rent', 'Date Available', 'Floor Plan']    
    with open(PATH, 'w',newline='') as f:
        # using csv.writer method from CSV package
        write = csv.writer(f)
        
        write.writerow(fields)
        write.writerows(data)

    return data,PATH

def crawler_Cortona():
    '''
    parse pricing information from Cortona's website
    returns a python list of pricing info
    '''
    URL = "https://www.cortonaforestpark.com/floorplans"

    # use selenium to fetch dynamic content
    options = webdriver.ChromeOptions()
    options.add_argument("--enable-javascript")
    # options.add_argument('headless')# this runs the task without opening a browser window

    driver = webdriver.Chrome(absPATH+'chromedriver.exe',options=options)
    driver.get(URL)

    # prevents driver shutting itself down
    time.sleep(1)

    # parse to soup with beautiful soup
    html = driver.page_source
    soup = BeautifulSoup(html,features="html.parser")

    # parse listing info to return data
    data = []
    floorPlans = soup.find_all(class_ = "card-title h4 font-weight-bold text-capitalize" )
    for floorPlan in floorPlans:
        data.append([floorPlan.text.strip()])
    
    avalibilities = soup.find_all(class_ = "d-block mb-2 font-weight-bold" )
    for i in range(len(floorPlans)):
        data[i].append(avalibilities[i].text.strip())
    
    startingPrices = soup.find_all(class_ = "p-2 fieldset bg-light border rounded d-flex flex-column align-items-center justify-content-center mb-2" )
    for i in range(len(floorPlans)):
        text = startingPrices[i].text.strip().replace("\n", "")
        data[i].append(" ".join(text.split()))# handles repeated whitespace
    
    # write result to csv file
    PATH = absPATH+f'pricingHistory/cortona/{date.today()}.csv'
    fields = ['FloorPlan', 'Availability', 'Rent']    
    with open(PATH, 'w',newline='') as f:
        # using csv.writer method from CSV package
        write = csv.writer(f)
        
        write.writerow(fields)
        write.writerows(data)
    
    return data,'dummyPath'

# test module
# data,PATH = crawler_Cortona()
# data,PATH = crawler_Encore()

# for i in data:
#     print(i)



