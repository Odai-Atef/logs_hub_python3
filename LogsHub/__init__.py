import logging
from datetime import datetime
import json
from decouple import AutoConfig
import requests
import os 
dir_path = os.path.abspath(os.curdir)
config = AutoConfig(search_path=dir_path)
def _log(msg, application, level,execution_time, environment, user_id=None, extra_data=None):
        now =str( int(datetime.now().timestamp()))
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
        logging.basicConfig(filename=config('DIR')+now+'.log', filemode='w', format='%(message)s')
        logging.warning(json.dumps(data))
        return data
    
def _notify(msg):
        url=""
        requests.post(url, data = {"message": json.dumps(msg), "channel": msg['application']})    


def warning(msg, application, execution_time, environment, user_id=None, extra_data=None):
        _log(msg, application,config('WARNING') ,execution_time, environment, user_id, extra_data)
        
def info(msg, application, execution_time, environment, user_id=None, extra_data=None):
        _log(msg, application,config('INFO') ,execution_time, environment, user_id, extra_data) 

def error(msg, application, execution_time, environment, user_id=None, extra_data=None):
        _log(msg, application,config('ERROR') ,execution_time, environment, user_id, extra_data)      

def critical(msg, application, execution_time, environment, user_id=None, extra_data=None):
        _notify(_log(msg, application,config('CRITICAL') ,execution_time, environment, user_id, extra_data))

