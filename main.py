from stream import Main
import time

global procs
procs = list()

def main(procs):
    mainObj = Main()
    actualProcesses = mainObj.exec(procs)
    return actualProcesses

while True:
    processes = main(procs)
    time.sleep(300) # 5 minutes




