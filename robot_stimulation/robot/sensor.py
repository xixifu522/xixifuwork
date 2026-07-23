import random
import time
import logging

log=logging.getLogger(__name__)

class Sensor:
    def __init__(self,time_inter,temp_thres,dist_thres,bat_thres):
        self.inter=time_inter
        self.temp=temp_thres
        self.dist=dist_thres
        self.bat=bat_thres
    
    def get_data(self):
        start_time_stamp=time.time()
        data={"timestamp":round(start_time_stamp,2),
              "temp":round(random.uniform(1,50),1),
              "dist":round(random.uniform(0,5),2),
              "bat":random.randint(0,100)}
        time.sleep(self.inter)
        log.info(f"当前采集的数据是{data}")
        return data
        