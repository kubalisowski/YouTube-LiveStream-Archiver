from this_stream import LiveStream, Record, ProcManager
import schedule, time

processes = []

def main(processes):
    liveStreams = LiveStream() # Get list of streams live
    manager = ProcManager()
    newStreams = manager.compareProcStream(manager.inactiveKiller(processes), liveStreams) # Dict of live, but not recording now streams
    if len(newStreams) > 0:
        rec = Record()
        for key, value in newStreams:
            processes.append(rec.startRecording(key, value))
        return processes
    else: # Zero new streams
        return list()

def test():
    print('2nd func')

schedule.every(5).minutes.do(main(processes))

while True:
    schedule.run_pending()
    time.sleep(1)










