import logging

logging.basicConfig(filename="Config/LogFIles/UMNWWCHS.log",
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filemode='w')
mainLogger = logging.getLogger('MainLogger')
mainLogger.setLevel(logging.DEBUG)
