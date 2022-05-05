import atexit
import logging
import os
import warnings
from zipfile import ZipFile

import ComparativeSupervisedLearning.Config.StaticResources as Rs

logging.basicConfig(filename=Rs.LOG_FILES_DIRECTORY + "/" + Rs.LOG_FILE_NAME,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filemode='w')
mainLogger = logging.getLogger('MainLogger')
mainLogger.setLevel(logging.DEBUG)
warnings.filterwarnings('ignore')


@atexit.register
def arch_logs():
    mainLogger.debug("Archive logs on application exit")
    with ZipFile(Rs.ARCH_FILE_NAME, 'w') as zipObj:
        mainLogger.debug("created Zip file")
        for filenames in os.walk(Rs.LOG_FILES_DIRECTORY):
            for filename in filenames:
                if filename == Rs.LOG_FILE_NAME:
                    file_path = os.path.join(Rs.LOG_FILES_DIRECTORY, Rs.LOG_FILE_NAME)
                    zipObj.write(file_path)
