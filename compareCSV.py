from csv_diff import load_csv, compare
from datetime import date,timedelta

absPATH = 'E:/Github_repos/EncorePriceCrawler/'

def compareCSV():
    prevCSV = load_csv(open(absPATH+f'pricingHistory/{date.today() - timedelta(days = 1)}.csv'),key='UnitID')
    currCSV = load_csv(open(absPATH+f'pricingHistory/{date.today()}.csv'),key='UnitID')
    diff = compare(prevCSV,currCSV)

    isChanged = False
    outputString = ''
    
    for i in diff:
        if len(diff[i]) != 0: 
            isChanged = True
            outputString += (f'{len(diff[i])} {i}:\n')
            if i == 'changed':
                for line in diff[i]:
                    unitID = line['key']
                    changes = line['changes']
                    unitFloorPlan = prevCSV[unitID]['Floor Plan']

                    outputString += (f'Unit: {unitID} ({unitFloorPlan})\n')
                    for dataField in changes:
                        outputString += (f'{dataField}: {changes[dataField][0]} => {changes[dataField][1]}\n')
                    outputString += '\n'
            else:
                outputString += str(diff[i])
                outputString += '\n'

    return outputString,isChanged

# # test module
# diff, changed = compareCSV()
# print(diff)