import requests
from flask import Flask, request, abort
from bs4 import BeautifulSoup
import json
from Project.Config import *

app = Flask(__name__)

@app.route('/pornhub', methods = ['POST','GET'])
def pornhub():
    if request.method == 'POST':
        
                    payload = request.json

        Reply_token = payload['events'][0]['replyToken']

        message = payload['events'][0]['message']['text']

        

        url = "https://www.xnxx.com/search/" + message

        data = requests.get(url)

        imgSrc = []

        i = 1

        linkTail = []

        ii = 1

        numberOfClips = 10

        clipCounter = 0

        soup = BeautifulSoup(data.text,'html.parser')

        for div in soup.find_all('div',{"class":"thumb"}):

            for getatag in div.find_all('a',href=True):

                print(getatag['href'])

                linkTail.append(getatag['href'])

                if ii >= numberOfClips:

                        break

                ii = ii +1

                for imgLink in getatag.find_all('img'):

                    imgSrc.append(imgLink['data-src'])

                    print(imgSrc)

                    if i >= numberOfClips:

                        break

                    i = i+1

                    clipCounter = clipCounter+ 1

            # numberOfClips = numberOfClips + 1

        i = 0

        fullLink = []

        for i in range(numberOfClips):

            fullLink.append("https://xnxx.com" + linkTail[i])

        ReplyMessage(Reply_token,fullLink,Channel_access_token,imgSrc,message,clipCounter)

        return request.json, 200

    elif request.method == 'GET' :

        return 'this is method GET!!!' , 200

    else:

        abort(400)


def ReplyMessage(Reply_token, Link, Line_Acees_Token, imgSrc, keyWord, count):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    Authorization = 'Bearer {}'.format('RAPsViFQbMGv5FvBgzr7gG8CASW9fAoJyyRHaiWraUDUo9bVWbpZdN+u6hxf+Fccliw/b0ZByZ/38RhNAE+hBRQLjumrkavdNu9shdxqmT3wU/hyPiI1FgchgUoC0TKrzryKYuqJN+9fyTqBRJ5pCgdB04t89/1O/w1cDnyilFU=')
    print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }
    if count >= 9 :
        data = {
        "replyToken":Reply_token,
        "messages":[{
  "type": "flex",
  "altText": "PNCK",
  "contents": {
    "type": "carousel",
    "contents": [
        #start first flex here
        content(imgSrc[0],Link[0],keyWord),
        content(imgSrc[1],Link[1],keyWord),
        content(imgSrc[2],Link[2],keyWord),
        content(imgSrc[3],Link[3],keyWord),
        content(imgSrc[4],Link[4],keyWord),
        content(imgSrc[5],Link[5],keyWord),
        content(imgSrc[6],Link[6],keyWord),
        content(imgSrc[7],Link[7],keyWord),
        content(imgSrc[8],Link[8],keyWord)

    ]
  }
}]
    }
    elif count >=7 :
                data = {
        "replyToken":Reply_token,
        "messages":[{
  "type": "flex",
  "altText": "PNCK",
  "contents": {
    "type": "carousel",
    "contents": [
        #start first flex here
        content(imgSrc[0],Link[0],keyWord),
        content(imgSrc[1],Link[1],keyWord),
        content(imgSrc[2],Link[2],keyWord),
        content(imgSrc[3],Link[3],keyWord),
        content(imgSrc[4],Link[4],keyWord),
        content(imgSrc[5],Link[5],keyWord),
        content(imgSrc[6],Link[6],keyWord)

    ]
  }
}]
    }
    elif count >=5 :
            data = {
        "replyToken":Reply_token,
        "messages":[{
  "type": "flex",
  "altText": "PNCK",
  "contents": {
    "type": "carousel",
    "contents": [
        #start first flex here
        content(imgSrc[0],Link[0],keyWord),
        content(imgSrc[1],Link[1],keyWord),
        content(imgSrc[2],Link[2],keyWord),
        content(imgSrc[3],Link[3],keyWord),
        content(imgSrc[4],Link[4],keyWord)

    ]
  }
}]
    }
    elif count >=3 :
            data = {
        "replyToken":Reply_token,
        "messages":[{
  "type": "flex",
  "altText": "PNCK",
  "contents": {
    "type": "carousel",
    "contents": [
        #start first flex here
        content(imgSrc[0],Link[0],keyWord),
        content(imgSrc[1],Link[1],keyWord),
        content(imgSrc[2],Link[2],keyWord)

    ]
  }
}]
    }
    else :
        data = {
        "replyToken":Reply_token,
        "messages":[{
  "type": "flex",
  "altText": "PNCK",
  "contents": {
    "type": "carousel",
    "contents": [
        #start first flex here
        content(imgSrc[0],Link[0],keyWord)
    ]
  }
}]
    }



    data = json.dumps(data) ## dump dict >> Json Object
    requests.post(LINE_API, headers=headers, data=data) 
    return 200
