from csv_diff import load_csv, compare
from datetime import date,timedelta

absPATH = 'E:/Github_repos/EncorePriceCrawler/'

def compareCSV():
    diff = compare(
        load_csv(open(absPATH+f'pricingHistory/{date.today() - timedelta(days = 1)}.csv'),key='UnitID'),
        load_csv(open(absPATH+f'pricingHistory/{date.today()}.csv'),key='UnitID')
    )
    isChanged = False
    for i in diff:
        if len(diff[i]) != 0: 
            isChanged = True
            return diff,isChanged
    
    return diff,isChanged

