from http.client import ImproperConnectionState
from crawler import crawler
from emailHandler import sendEmail
from compareCSV import compareCSV

URL = "https://encore.securecafe.com/onlineleasing/encore-at-forest-park/rentaloptions.aspx?MoveInDate=7/1/2022"
data,attPath = crawler(URL)

# TODO: storing mail info in plain text might not be safe
mailList = ["sodabiy@gmail.com",'394309448@qq.com','zhangyy_2020@outlook.com']

diff,isChanged = compareCSV()

for receiver in mailList:
    sendEmail(receiver,attPath,isChanged,diff)

# sendEmail(mailList[0],attPath,isChanged,diff)

print('Daily Digest Sent')