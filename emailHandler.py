import yagmail
import json

absPATH = 'E:/Github_repos/EncorePriceCrawler/'

def sendEmail(receiver,filename,isChanged,changes):
    '''
    handles emailing using yagmail library
    '''
    bfJSONString = json.dumps(changes, sort_keys=True, indent=4)

    if isChanged:
        body = '<h1>HEY! Change in listing detected!</h1>'+'<br>'+bfJSONString
        filename = filename
    else:
        body = '<h1>No changes detected, better luck tomorrow :)</h1>'
        filename = filename

    yag = yagmail.SMTP("nochancedev@gmail.com",oauth2_file=absPATH+'credentials.json')
    yag.send(
        to=receiver,
        subject="Daily Digist of House Pricing",
        contents=body, 
        attachments=filename,
    )