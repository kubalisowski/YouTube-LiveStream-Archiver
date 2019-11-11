import multiprocessing
from stream import Record, LiveStream

def main(liveStreams):


    pass




liveProcess = []

if __name__ == '__main__':
    proc = multiprocessing.Process(target=main, args=())
    for l in liveProcess:
        if l.is_alive() == False:
               liveProcess.remove(l)
        else:
            if proc.name != l.name:
                ### Start process and add to live streams list
                liveProcess.append(proc.start())
            else:
                pass







