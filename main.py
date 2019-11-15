from stream import LiveStream, Record

procs = []

def main(processes):
    streams = LiveStream()
    for key, value in streams.liveStreams.items():
        rec = Record(key, value)
        processes.append(rec.startRecording())
    return processes

m = main(procs)
print(m)

# while True:
#     for p in procs:
#         if p.poll() == None:
#             print(p.name)






