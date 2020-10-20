import logging
from datetime import datetime
import json
from decouple import AutoConfig
import requests
import os 

	
dir_path = os.path.abspath(os.curdir)
config = AutoConfig(search_path=dir_path)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

con = logging.StreamHandler()
con.setLevel(logging.INFO)

formatter = logging.Formatter('%(message)s')
con.setFormatter(formatter)
logger.addHandler(con)

def _log(msg, application, level,execution_time, user_id, extra_data):
        now =str( int(datetime.now().timestamp()))    
        environment = 'development' if config("ENVIRONMENT") == None or config("ENVIRONMENT")=="" else config("ENVIRONMENT")
        application = 'unknown' if config("APPLICATION") == None or config("APPLICATION")=="" else config("APPLICATION")

        data={
            "message": msg,
            "level": level,
            "application": application,
            "environment": environment,
            "user_id": user_id,
            "execution_time": execution_time,
            "extra_data": extra_data,
            "timestamp": now
        }

        handler = logging.FileHandler(config('DIR')+now+'.log')
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler) 

        logger.warning(json.dumps(data))
        logger.removeHandler(handler)

        return data
    
def _notify(msg):
        url=config("NOTIFY_URL")
        requests.post(url, data = {"message": json.dumps(msg), "channel": msg['application']})    


def warning(msg, application=None,  execution_time=None, user_id=None, extra_data=None):
        _log(msg, application,config('WARNING') ,execution_time, user_id, extra_data)
        
def info(msg, application=None,  execution_time=None, user_id=None, extra_data=None):
        _log(msg, application,config('INFO') ,execution_time, user_id, extra_data) 

def error(msg, application=None,  execution_time=None, user_id=None, extra_data=None):
        _log(msg, application,config('ERROR') ,execution_time, user_id, extra_data)      

def critical(msg, application=None,  execution_time=None, user_id=None, extra_data=None):
        _notify(_log(msg, application,config('CRITICAL') ,execution_time, user_id, extra_data))


