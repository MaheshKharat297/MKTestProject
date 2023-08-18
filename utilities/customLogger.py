import inspect
import logging
import os
import configparser


class LogGen:
    @staticmethod
    def loggen():
        #logging.basicConfig(filename="./Logs/automation.log",
                            #format="%(asctime)s: %(levelname)s: %(message)s")
        #logger = logging.getLogger()
        #logger.setLevel(logging.INFO)
        #return logger
        logger = logging.getLogger()
        filehandler = logging.FileHandler("./Logs/automation.log")
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger
