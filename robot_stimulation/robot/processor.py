import logging
log=logging.getLogger(__name__)

class Processor:
    def __init__(self,temp_thres,dist_thres,bat_thres):
        self.temp=temp_thres
        self.dist=dist_thres
        self.bat=bat_thres
    
    def judge_state(self,data):
        temp=data["temp"]
        dist=data["dist"]
        bat=data["bat"]
        if temp > self.temp:
           state= "高温预警"
        elif dist < self.dist:
            state="有障碍，停车"
        elif bat < self.bat:
            state="电量低，返航"
        else:
            state= "正常运行"
        log.info(f"处理器接受数据{data},判断结果{state}")
        return state