from robot import Sensor,Processor,Control
if __name__=="__main__":
    time_inter=2
    temp_thres=40
    dist_thres=4
    bat_thress=75

    sensor1=Sensor(time_inter,temp_thres,dist_thres,bat_thress)
    processor1=Processor(temp_thres,dist_thres,bat_thress)
    control1=Control()

    data=sensor1.get_data()
    print("采集数据:",data)
    judge_data=processor1.judge_state(data)
    control1.get_cmd(judge_data)




