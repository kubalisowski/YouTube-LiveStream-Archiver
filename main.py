#import youtube_dl
import subprocess
import requests
import json

class Vars:
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    baseUrl = 'https://www.youtube.com/watch?v='
    channels = {'rafatus': 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UC9gkwh2D2Vo_0YNB-q71d1A&type=video&eventType=live&key=AIzaSyBFB6euD6FKO6OwixkSENe4FJtejE1ahXw',
                'Telewizja wPolsce' : 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCPiu4CZlknkTworskK79CPg&type=video&eventType=live&key=AIzaSyBFB6euD6FKO6OwixkSENe4FJtejE1ahXw',
                'Rzeczpospolita TV' : 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCpchzx2u5Ab8YASeJsR1WIw&type=video&eventType=live&key=AIzaSyBFB6euD6FKO6OwixkSENe4FJtejE1ahXw',
                }

class LiveStream(Vars):
    ### Returns urls list of live streams
    def checkLive(self):
        liveStreams = []
        for key, value in self.channels.items():
            response = requests.get(value, self.headers).text
            jason = json.loads(response)

            if jason['pageInfo']['totalResults'] == 1:
                videoUrl = self.baseUrl + jason['items']['id']['videoId']
                liveStreams.append(videoUrl)
            return liveStreams

    def startRecord(self, liveStreams):
        for s in liveStreams:
            subprocess.Popen(['youtube-dl', s], shell=False)

record = LiveStream()
check = record.checkLive()
record.startRecord(check)



