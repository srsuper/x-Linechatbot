Channel_secret= 'e9471ddf5803bd36ea98304e74b190b4'
Channel_access_token = 'iM0cqxFMtiLnAGpI4g9bZjtssFBl0bkL1qXeHAMkdiGOldPbVPDg6pE+rb4JSQI6SJbd8blc4PyB7zSNRB1YDUweSz00AACauvGc2S8h4KtktH7gyBTEhEKXeSXfcNP5mYqqEDl9A9hRHyl91+SGRQdB04t89/1O/w1cDnyilFU='

def content(imgSrc,Link,KW):
    return {
    "type": "bubble",
    "header": {
      "type": "box",
      "layout": "horizontal",
      "contents": [
        {
          "type": "text",
          "text": KW.title(),
          "size": "xl",
          "align": "start",
          "weight": "bold",
          "color": "#951DFF",
          "wrap": True
        }
      ]
    },
    "hero": {
      "type": "image",
      "url": imgSrc,
      "size": "full",
      "aspectRatio": "20:13",
      "aspectMode": "cover",
      "action": {
        "type": "uri",
        "label": "Action",
        "uri": Link
      }
    },
    "footer": {
      "type": "box",
      "layout": "horizontal",
      "contents": [
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "Watch Now",
            "uri": Link
          },
                    "color": "#951DFF",
          "height": "sm",
          "style": "primary"
        }
      ]
    }
  }