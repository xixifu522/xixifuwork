import logging
log=logging.getLogger(__name__)



class Control:
    def get_cmd(self,judge_data):
        log.info(f"控制器输出指令{judge_data}")
        return judge_data