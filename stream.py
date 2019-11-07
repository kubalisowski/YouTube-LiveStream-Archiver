import subprocess
import requests
import json
from config import Config

class LiveStream(Config):
    ### Returns urls list of live streams
    def isLive(self):
        liveStreams = []
        for key, value in self.channels.items():
            response = requests.get(value, self.headers).text
            jason = json.loads(response)

            if jason['pageInfo']['totalResults'] == 1:
                videoUrl = self.baseUrl + jason['items']['id']['videoId']
                liveStreams.append(videoUrl)
            return liveStreams

class Record:
    def __init__(self, videoUrl):
        self.videoUrl = videoUrl

    def startRecording(self):
        for v in self.videoUrl
        subprocess.Popen(['youtube-dl', self.videoUrl], shell=False)






