from csv_diff import load_csv, compare
from datetime import date,timedelta
import json

absPATH = 'E:/Github_repos/EncorePriceCrawler/'

def compareCSV():
    prevCSV = load_csv(open(absPATH+f'pricingHistory/{date.today() - timedelta(days = 1)}.csv'),key='UnitID')
    currCSV = load_csv(open(absPATH+f'pricingHistory/{date.today()}.csv'),key='UnitID')
    diff = compare(prevCSV,currCSV)

    isChanged = False
    for i in diff:
        if len(diff[i]) != 0: 
            isChanged = True
            return diff,isChanged
    
    return diff,isChanged

diff, changed = compareCSV()

for i in diff:
    if diff[i]:
        print(f'{len(diff[i])} {i}:')
        if i == 'changed':
            for line in diff[i]:
                UnitID = line['key']
                changes = line['changes']
                print(f'    UnitID: {UnitID}')
                for dataField in changes:
                    print(f'        {dataField}: {changes[dataField][0]} => {changes[dataField][1]}')
        else:
            print(diff[i])
    print('\n')