import subprocess
import requests
import json
from test_config import Config

class ProcManager:
    def inactiveKiller(self, processes): #  # Delete inactive subprocess object (subrocess_object.poll() != None)
        for p in processes:
            if p.poll() != None:
                processes.remove(p)
        return processes

    def compareProcStream(self, processes, liveStreams): # Def returns dict of stremas to start be recording
        if processes == 0:
            return liveStreams # No processes running thus all live streams can be recorder
        else:
            if liveStreams > 0: # 1 on more live streams
               for p in processes:
                   keys = tuple(liveStreams.keys())
                   for key in keys:
                       if p.name == key:
                           del liveStreams[key]
                newStreams = liveStreams # # Dict of live, but not recording now streams (just naming change)
                return newStreams
            else:
                return dict() # Zero live streams returns empty dict object

class Record():
    def startRecording(self, channelName, videoUrl):
        proc = subprocess.Popen(['youtube-dl', videoUrl], shell=False)
        proc.name = channelName
        return proc

class LiveStream(Config):
    liveStreams = {} ### liveStreams variable is dict {channel_name : livestream_url,}
    for key, value in Config.channels.items():
        jason = json.loads(requests.get(value, Config.headers).text)
        if jason['pageInfo']['totalResults'] == 1:
            liveStreams.update({key : Config.baseUrl + jason['items'][0]['id']['videoId']})









