import logging
from datetime import datetime
import json
from decouple import config
import requests

def main():
    return None
class logs_hub:


    def _log(self,msg, application, level,execution_time, user_id, extra_data):
        now =str( int(datetime.now().timestamp()))
        environment = 'development' if config("ENVIRONMENT") == None or config("ENVIRONMENT")=="" else config("ENVIRONMENT")
        application = 'unknown' if config("APPLICATION") == None or config("APPLICATION")=="" else config("APPLICATION")
        if(application == 'unknown'): print("!!! ERROR: APPLICATION NAME NOT SET IN ENVIRONMENT FILE, LOGSHUB WILL RECORD APPLICATION NAME AS 'unknown'")
        
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
        logging.basicConfig(filename=now+'.log', filemode='w', format='%(message)s')
        logging.warning(json.dumps(data))
        return data
    
    def _notify(self,msg):
        url=config("NOTIFY_URL")
        requests.post(url, data = {"message": json.dumps(msg), "channel": msg['application']})


    def warning(self,msg, application=None, execution_time=None, user_id=None, extra_data=None):
        self._log(msg, application,config('WARNING') ,execution_time,  user_id, extra_data)
        
    def info(self,msg, application=None, execution_time=None, user_id=None, extra_data=None):
        self._log(msg, application,config('INFO') ,execution_time,  user_id, extra_data) 

    def error(self,msg, application=None, execution_time=None, user_id=None, extra_data=None):
        self._log(msg, application,config('ERROR') ,execution_time,  user_id, extra_data)      

    def critical(self,msg, application=None, execution_time=None, user_id=None, extra_data=None):
        self._notify(self._log(msg, application,config('CRITICAL') ,execution_time,  user_id, extra_data))

