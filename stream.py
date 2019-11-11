import subprocess
import requests
import json
from config import Config

class LiveStream(Config):
    ### Returns dict of live streams jasons + names from config
    def isLive(self):
        liveStreams = []
        for key, value in self.channels.items():
            response = requests.get(value, self.headers).text
            jason = json.loads(response)

            if jason['pageInfo']['totalResults'] == 1:
                liveStreams[key] = jason
            return liveStreams

    def startRecording(self):
        videoUrl = self.baseUrl + self.liveStream['items']['id']['videoId']
        proc = subprocess.Popen(['youtube-dl', videoUrl], shell=False, name=self.name)
        return proc











