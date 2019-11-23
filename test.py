# from config import *
# from stream import *
#
# org = OrganizeFiles()
#
# org1 = org.execute('Telewizja wPolsce')
# print(org1)

import os
from stream import *

org = OrganizeFiles()
path = org.execute('Telewizja wPolsce')
if not os.path.exists(path):
    os.makedirs(path)




