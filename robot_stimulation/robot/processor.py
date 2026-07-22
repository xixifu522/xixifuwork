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
           return "高温预警"
        elif dist < self.dist:
            return"有障碍，停车"
        elif bat < self.bat:
            return"电量低，返航"
        else:
            return "正常运行"
        