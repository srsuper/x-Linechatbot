Channel_secret= 'af18ea15041fc267d82f8d3b70eb5fc4'
Channel_access_token = 'RAPsViFQbMGv5FvBgzr7gG8CASW9fAoJyyRHaiWraUDUo9bVWbpZdN+u6hxf+Fccliw/b0ZByZ/38RhNAE+hBRQLjumrkavdNu9shdxqmT3wU/hyPiI1FgchgUoC0TKrzryKYuqJN+9fyTqBRJ5pCgdB04t89/1O/w1cDnyilFU='
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
            "label": "ดูคลิปนี้",
            "uri": Link
          },
                    "color": "#ff1d1d",
          "height": "sm",
          "style": "primary"
        }
      ]
    }
  }
