import logging
import os
from zipfile import ZipFile
from os.path import basename
import atexit

import ComparativeSupervisedLearning.Config.StaticResourcesPaths as Rs

logging.basicConfig(filename=Rs.LOG_FILES_DIRECTORY + "/" + Rs.LOG_FILE_NAME,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filemode='w')
mainLogger = logging.getLogger('MainLogger')
mainLogger.setLevel(logging.DEBUG)


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
