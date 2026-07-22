from robot import Sensor,Processor,Control
import os
from read_config import load_config

if __name__=="__main__":
    cfg=load_config("config/robot_config.json")
    if cfg is None:
        print("配置读取失败，程序退出")
        exit()

    time_inter=cfg["time_inter"]
    temp_thres=cfg["temp_thres"]
    dist_thres=cfg["dist_thres"]
    bat_thres=cfg["bat_thres"]

    sensor1=Sensor(time_inter,temp_thres,dist_thres,bat_thres)
    processor1=Processor(temp_thres,dist_thres,bat_thres)
    control1=Control()



    data=sensor1.get_data()
    print("采集数据:",data)
    judge_data=processor1.judge_state(data)
    control1.get_cmd(judge_data)




