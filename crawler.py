from attr import attr
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import yagmail
import csv
from datetime import date,datetime

absPATH = 'E:/Github_repos/EncorePriceCrawler/'

def crawler(URL):
    '''
    parse pricing information from encore's website
    returns a python list of pricing infor
    '''
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

    # # prints out the whole thing, test purpose
    # print(soup.get_text())

    # mapping of floor plan -> element id
    # TODO:THIS IS NOT A COMPREHENSIVE MAPPING! THERE ARE OTHER FLOOR PLANS!
    # floorPlanIdMap = {'A1 - 1b1b':'divFPH_2322187',
    #         'B2 - 2b2b':'divFPH_2322194',
    #         'B2B - 2b2b':'divFPH_2322196',
    #         'B3 - 2b2b':'divFPH_2322197',
    #         'C1 - 3b2b':'divFPH_2322198',
    #         'S1 - studio':'divFPH_2322186',
    #         'cock':'cock'
    # }

    # floorPlanTables = {}

    # parse a table, specific floor plan
    # for fp in floorPlanIdMap:
    #     data = []
    #     allTables = soup.find_all('table',id=floorPlanIdMap[fp])
    #     # print(allTables)
    #     for table in allTables:
    #         table_body = table.find('tbody')

    #         rows = table_body.find_all('tr')
    #         for row in rows:
    #             cols = row.find_all('td')
    #             cols = [ele.text.strip() for ele in cols]
    #             data.append([ele for ele in cols if ele]) # Get rid of empty values
        
    #     floorPlanTables[fp] = data

    # for fp in floorPlanTables:
    #     print(f'Table for {fp}: ')
    #     for i in floorPlanTables[fp]:
    #         print(i)

    # parse all table, no specific floor plan
    data = []
    allTables = soup.find_all('table')
    for table in allTables:
        table_body = table.find('tbody')

        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele]) # Get rid of empty values

    # last few tables are calendar info, irrelavent
    data = data[:-6]

    # write result to csv file
    PATH = absPATH+f'pricingHistory/{date.today()}_{datetime.now().strftime("%H_%M_%S")}.csv'
    fields = ['Unit', 'Sq.Ft.', 'Rent', 'Date Available']    
    with open(PATH, 'w') as f:
        # using csv.writer method from CSV package
        write = csv.writer(f)
        
        write.writerow(fields)
        write.writerows(data)

    return data,PATH

def sendEmail(receiver,filename):
    '''
    handles emailing using yagmail library
    '''
    body = 'Daily Digist of House Pricing at Encore, Enjoy.'

    yag = yagmail.SMTP("nochancedev@gmail.com",oauth2_file=absPATH+'credentials.json')
    yag.send(
        to=receiver,
        subject="Daily Digist of House Pricing",
        contents=body, 
        attachments=filename,
    )

URL = "https://encore.securecafe.com/onlineleasing/encore-at-forest-park/rentaloptions.aspx?MoveInDate=7/1/2022"
data,attPath = crawler(URL)
mailList = ["sodabiy@gmail.com",'394309448@qq.com','zhangyy_2020@outlook.com']

for receiver in mailList:
    sendEmail(receiver,attPath)

# sendEmail(mailList[0],attPath)

print('Daily Digest Sent')


