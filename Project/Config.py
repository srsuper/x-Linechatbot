Channel_secret= '081acf8c67cd1920fe5f620834497b5f'
Channel_access_token = '9hNPs1IxuzZgqLJiIwAokUwN2Gqbo/GMYvrkdogt2y64sC1R2myGzTbV90IrMwf5cB1tOXTIpGX0PosZVeMxv9tRRL1Nn3aMgoi1RFI7DonLX3oEYcXYopFvGFhHXmzEmf+vehz/69rOcfeXSuSTSgdB04t89/1O/w1cDnyilFU='
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
