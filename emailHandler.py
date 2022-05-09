import yagmail

absPATH = 'E:/Github_repos/EncorePriceCrawler/'

def sendEmail(receiver,attachments,isChanged,changes):
    '''
    handles emailing using yagmail library
    '''

    if isChanged:
        body = '<h1>HEY! Change in listing detected!</h1>'+'<br>'
        for i in changes:
            body+=i
    else:
        body = '<h1>No changes detected, better luck tomorrow :)</h1>'

    yag = yagmail.SMTP("nochancedev@gmail.com",oauth2_file=absPATH+'credentials.json')
    yag.send(
        to=receiver,
        subject="Daily Digist of House Pricing",
        contents=body, 
        attachments=attachments,
    )