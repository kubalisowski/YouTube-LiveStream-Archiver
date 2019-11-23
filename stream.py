import subprocess
import requests
import json
from config import Config, ChannelsAPI
import os

class ProcManager:
    def inactiveKiller(self, processes):  # Delete inactive subprocess object (subprocess_object.poll() != None)
        if processes != None or processes > 0:
            for p in processes:
                if p.poll() != None:
                    processes.remove(p)
            return processes
        else:
            processes = list() # Prevent NoneType
            return processes


    def compareProcStream(self, processes, liveStreams):  # Def returns dict of streams to start be recording
        if len(processes) == 0:
            return liveStreams  # No processes running thus all live streams can be recorder
        else:
            if len(liveStreams) > 0:  # 1 on more live streams
                for p in processes:
                    keys = tuple(liveStreams.keys())
                    for key in keys:
                        if p.name == key:
                            del liveStreams[key]
                return liveStreams   # Dict of live, but not recording now streams
            else:
                return dict()  # Zero live streams returns empty dict object


class LiveStream(ChannelsAPI):   # ChannelsAPI inherits Config
    liveStreams = {}  # { channel_name : livestream_url }
    for key, value in ChannelsAPI.channels.items():
        jason = json.loads(requests.get(value, Config.headers).text)  # JSON response from api link
        if jason['pageInfo']['totalResults'] == 1:
            liveStreams.update({key: Config.baseUrl + jason['items'][0]['id']['videoId']})


class OrganizeFiles(ChannelsAPI):  # ChannelAPI inherits from Config
    def execute(self, channelName):
        downloadPath = str()
        nextDir = r'/'   # For download path creation
        for channel, apiUrl in ChannelsAPI.channels.items():
            if channel == channelName:
                jason = json.loads(requests.get(apiUrl, Config.headers).text)
                downloadPath = Config.mainDownloadPath + nextDir + channel + nextDir + Config.year + Config.month + Config.day
        return downloadPath
            

class Record(Config):
    def startRecording(self, channelName, videoUrl, downloadPath):
        proc = subprocess.Popen(['youtube-dl', videoUrl], shell=False, cwd=downloadPath)
        proc.name = channelName
        return proc


class Main(ProcManager, Record, LiveStream):
    def exec(self, processes):
        liveStreams = LiveStream()  # Get list of streams live
        manager = ProcManager()
        manager.inactiveKiller(processes)

        newStreams = manager.compareProcStream(manager.inactiveKiller(processes), liveStreams.liveStreams) # Dict of live, but not recording now streams
        lenghtStreams = len(newStreams)

        if lenghtStreams > 0:
            for name, videoUrl in newStreams.items():
                dirs = OrganizeFiles()
                saveFilePath = dirs.execute(name)
                if not os.path.exists(saveFilePath):  # Creating folder structure if not exist
                    os.makedirs(saveFilePath)
                rec = Record()
                processes.append(rec.startRecording(name, videoUrl, str(saveFilePath)))  # Subpropcess will run, so file will be saved: channel_na>>date>>videoname.mp4
            return processes
        else: # Zero new streams
            return list()
