from http.client import ImproperConnectionState
from crawler import crawler_Encore,crawler_Cortona
from emailHandler import sendEmail
from compareCSV import compareCSV_cortona,compareCSV_encore

data_Encore,attPath_Encore = crawler_Encore()
data_Encore,attPath_Cortona = crawler_Cortona()
attPath = [attPath_Encore,attPath_Cortona]


# insert recipents mail address in mailList
mailList = []

diffEncore,isChangedEncore = compareCSV_encore()
diffCortona,isChangedCortona = compareCSV_cortona()

diff = [diffEncore,diffCortona]
changed = (isChangedEncore and isChangedCortona)

# send to all
for receiver in mailList:
    sendEmail(receiver,attPath,changed,diff)

# FOR TEST: Send to dev
# sendEmail(mailList[0],attPath,changed,diff)

print('Daily Digest Sent')