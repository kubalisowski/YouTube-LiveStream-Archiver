class Config:
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

    baseUrl = 'https://www.youtube.com/watch?v='

    auth2 = 'AIzaSyBFB6euD6FKO6OwixkSENe4FJtejE1ahXw'
    auth = 'AIzaSyBag5dZLIOwtU-UO8Cr8iXK4Gv0ZV8VmLU'

    channels = {'rafatus': 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCeAun7EBsIyk-1jYGx2NLeg&type=video&eventType=live&key=' + auth, 'Telewizja wPolsce' : 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCPiu4CZlknkTworskK79CPg&type=video&eventType=live&key=' + auth, 'Rzeczpospolita TV' : 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCpchzx2u5Ab8YASeJsR1WIw&type=video&eventType=live&key=' + auth,}

# Content warning -- check if YouTube account can access stream via browser
# 'rafatus': 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCeAun7EBsIyk-1jYGx2NLeg&type=video&eventType=live&key=' + auth