from stream import LiveStream

stream = LiveStream()
rec = stream.startRecording()

### If .poll() returns None process is live
for r in rec:
    print(r.poll())











