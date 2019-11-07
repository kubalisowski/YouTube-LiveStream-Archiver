class Config:
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

    baseUrl = 'https://www.youtube.com/watch?v='

    channels = {'rafatus': 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UC9gkwh2D2Vo_0YNB-q71d1A&type=video&eventType=live&key=AIzaSyBFB6euD6FKO6OwixkSENe4FJtejE1ahXw',
                'Telewizja wPolsce' : 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCPiu4CZlknkTworskK79CPg&type=video&eventType=live&key=AIzaSyBFB6euD6FKO6OwixkSENe4FJtejE1ahXw',
                'Rzeczpospolita TV' : 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCpchzx2u5Ab8YASeJsR1WIw&type=video&eventType=live&key=AIzaSyBFB6euD6FKO6OwixkSENe4FJtejE1ahXw',
                }