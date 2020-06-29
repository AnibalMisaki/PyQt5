import os, logging
from logging.handlers import RotatingFileHandler

class logger(object):

    __instance = None # Save the instance of the class itself
    __Initialized = False # Flag if already initialized
    __app_log = None

    def __init__(self):
        if  not self.__Initialized:
            __program_files = "/opt" #os.environ["ALLUSERSPROFILE"]
            if not os.path.exists("%s/Sistema SCADA" % __program_files): # if does not exist, is created
                os.makedirs("%s/Sistema SCADA" % __program_files)
            __log_formatter = logging.Formatter('[Desktop SCADA] [%(asctime)s] [%(levelname)s] %(message)s','%d/%m/%Y %H:%M')
            __logFile = '%s/Sistema SCADA/SCADA.log' % __program_files
            __my_handler = RotatingFileHandler(__logFile, maxBytes=5242880,
                                                backupCount=2, encoding=None, delay=0)
            __my_handler.setFormatter(__log_formatter)
            __my_handler.setLevel(logging.INFO)
            self.__app_log = logging.getLogger()
            self.__app_log.setLevel(logging.INFO)
            self.__app_log.addHandler(__my_handler)
            self.__Initialized = True

    def __new__(cls,*args,**kwargs ):        
        if cls.__instance is None :
            cls.__instance =  super(logger,cls).__new__(cls)   
        return cls.__instance

    def log_error(self,e:Exception):
        self.__app_log.error("¡Error! %s" % str(e),exc_info=True)
    
    def log_traceback(self,traceback):
        self.__app_log.info(traceback)

    def log_info(self,e):
        self.__app_log.info("¡Info! %s" % str(e))