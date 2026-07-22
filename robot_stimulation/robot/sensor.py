import random
import time

class Sensor:
    def __init__(self,time_inter,temp_thres,dist_thres,bat_thres):
        self.inter=time_inter
        self.temp=temp_thres
        self.dist=dist_thres
        self.bat=bat_thres
    
    def get_data(self):
        time_sample=time.time()
        data={"timesample":round(time_sample,2),
              "temp":round(random.uniform(1,50),1),
              "dist":round(random.uniform(0,5),2),
              "bat":random.randint(0,100)}
        return data
        