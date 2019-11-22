from stream import Main
import time

global procs
procs = list()

def main(processes):
    mainObj = Main()
    actualProcesses = mainObj.exec(processes)
    return actualProcesses

while True:
    procs = main(procs)
    time.sleep(300) # 5 minutes




