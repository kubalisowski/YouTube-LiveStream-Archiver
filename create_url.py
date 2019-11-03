baseUrl = ['https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=', '&type=video&eventType=live&key=AIzaSyBFB6euD6FKO6OwixkSENe4FJtejE1ahXw']

channelId = input('CHANNEL-ID: ')

def createUrl(channelId):
    url = baseUrl[0] + channelId + baseUrl[1]

    return print(url)

result = createUrl(channelId)






