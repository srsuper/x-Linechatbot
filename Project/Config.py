Channel_secret= 'YOUR_CHANNEL_SECRET'
Channel_access_token = 'YOUR_CHANNEL_ACCESS_TOKEN'
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
