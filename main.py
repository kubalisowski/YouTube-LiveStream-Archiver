from teststream import LiveStream, Record

processes1 = []

### To be put into schedule
def main(processes):
    live = LiveStream()
    streams = live.liveStreams
    for key, value in streams.items():
        if len(processes) == 0:
            rec = Record(key, value)
            processes.append(rec.startRecording())
    return processes
                # if p.poll() == None:
                #     if p.name
                #     rec = Record()
                #     processes.append(rec.startRecording(key, value))

xxx = main(processes1)
for x in xxx:
    print(x.name)





