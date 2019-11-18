from stream import LiveStream, Record, ProcManager, Main
import schedule, time

global procs

def main(procs):
    mainObj = Main()
    actualProcesses = mainObj.exec(procs)
    return actualProcesses

procs = list()
mn = main(procs)
# print(mn)

# schedule.every(0).minutes.do(main)
#
while True:
    # schedule.run_pending()
    processes = main(procs)
    for p in processes:
        print(p.name)
    time.sleep(1)




