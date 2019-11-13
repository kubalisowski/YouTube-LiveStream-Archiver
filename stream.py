import subprocess
import requests
import json
from config import Config

class LiveStream(Config):
    liveStreams = {}
    for key, value in Config.channels.items():
        jason = json.loads(requests.get(value, Config.headers).text)
        if jason['pageInfo']['totalResults'] == 1:
            liveStreams.update({key : jason})

    def startRecording(self):
        processes = []
        for key, value in self.liveStreams.items():
            videoUrl = self.baseUrl + value['items'][0]['id']['videoId']
            proc = subprocess.Popen(['youtube-dl', videoUrl], shell=False)
            ### Set name to each process
            proc.name = key
            processes.append(proc)
        return processes












