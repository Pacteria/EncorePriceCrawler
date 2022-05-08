from http.client import ImproperConnectionState
from crawler import crawler_Encore
from emailHandler import sendEmail
from compareCSV import compareCSV

data_Encore,attPath_Encore = crawler_Encore()

# TODO: storing mail info in plain text might not be safe
mailList = ["sodabiy@gmail.com",'394309448@qq.com','zhangyy_2020@outlook.com']

diffEncore,isChangedEncore = compareCSV('encore')

# TODO: decide if we have to do 2 emails 
# or can we make it one

# for receiver in mailList:
#     sendEmail(receiver,attPath_Encore,isChangedEncore,diffEncore)

sendEmail(mailList[0],attPath_Encore,isChangedEncore,diffEncore)

print('Daily Digest Sent')