from csv_diff import load_csv, compare
from datetime import date,timedelta

absPATH = 'E:/Github_repos/EncorePriceCrawler/'

def compareCSV_encore():
    prevCSV = load_csv(open(absPATH+f'pricingHistory/encore/encore_{date.today() - timedelta(days = 1)}.csv'),key='UnitID')
    currCSV = load_csv(open(absPATH+f'pricingHistory/encore/encore_{date.today()}.csv'),key='UnitID')
    diff = compare(prevCSV,currCSV)

    isChanged = False
    outputString = '<h2>Encore:</h2>\n'
    
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

def compareCSV_cortona():
    prevCSV = load_csv(open(absPATH+f'pricingHistory/cortona/cortona_{date.today() - timedelta(days = 1)}.csv'),key='FloorPlan')
    currCSV = load_csv(open(absPATH+f'pricingHistory/cortona/cortona_{date.today()}.csv'),key='FloorPlan')
    diff = compare(prevCSV,currCSV)

    isChanged = False
    outputString = '<h2>Cortona:</h2>\n'
    
    for i in diff:
        if len(diff[i]) != 0: 
            isChanged = True
            outputString += (f'{len(diff[i])} {i}:\n')
            if i == 'changed':
                for line in diff[i]:
                    FloorPlan = line['key']
                    changes = line['changes']

                    outputString += (f'FloorPlan: {FloorPlan} \n')
                    for dataField in changes:
                        outputString += (f'{dataField}: {changes[dataField][0]} => {changes[dataField][1]}\n')
                    outputString += '\n'
            else:
                outputString += str(diff[i])
                outputString += '\n'

    return outputString,isChanged

# test module
# diff, changed = compareCSV_encore()
# print(diff)
# diff, changed = compareCSV_cortona()
# print(diff)