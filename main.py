#################################################################################
########## https://developers.google.com/youtube/v3/getting-started #############
########## LAST DONE: UNKNOWN -- DAY LIMIT FOR AUTH KEY EXPIRED #################
#################################################################################
from stream import LiveStream, Record, ProcManager, Main
import schedule, time



def main(procs):
    mainObj = Main()
    actualProcesses = mainObj.exec(procs)
    return actualProcesses

procs = []
mn = main(procs)
# print(mn)

# schedule.every(0).minutes.do(main)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)
#     processes = main()
#     if len(processes) > 0:
#         print(processes)






