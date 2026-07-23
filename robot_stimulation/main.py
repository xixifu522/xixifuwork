from robot import Sensor,Processor,Control
import os
from read_config import load_config
from logger import loggers
from queue_until import put_last
import time
import queue
import threading

log=loggers()

def sensor_producer(sensor1:Sensor,sen_queue:queue.Queue,stop_sig:threading.Event,max_q_len):
    log.info("传感器采集数据线程启动")
    while not stop_sig.is_set():
        try:
            data=sensor1.get_data()
            put_last(sen_queue,data,max_q_len)
            log.info(f"采集数据{data}入列")
        except Exception as e:
            log.error(f"采集数据异常{e}")
    log.info("传感器采集数据线程退出")


def processor_consumer(processor1:Processor,sen_queue:queue.Queue,pro_queue:queue.Queue,stop_sig:threading.Event,max_q_len):
    log.info("数据处理线程启动")
    while not stop_sig.is_set():
        try:
            state_data=sen_queue.get(timeout=0.2)
            state=processor1.judge_state(state_data)
            if "高温" in state or "停车" in state or "返航" in state:
                  log.warning(f"异常状态{state}")
            else:
                  log.info(f"正常状态{state}")
            put_last(pro_queue,state,max_q_len)

        except queue.Empty:
            continue
        except Exception as e:
            log.error(f"数据处理异常{e}")
    log.info("数据处理程序退出")        

        
if __name__=="__main__":
    cfg=load_config("config/robot_config.json")
    if cfg is None:
        log.error("配置读取失败，程序退出")
        exit()

    time_inter=cfg["time_inter"]
    temp_thres=cfg["temp_thres"]
    dist_thres=cfg["dist_thres"]
    bat_thres=cfg["bat_thres"]
    max_run_time=cfg["max_runseconds"]
    max_q_len=cfg["queue_max_len"]

    sensor1=Sensor(time_inter,temp_thres,dist_thres,bat_thres)
    processor1=Processor(temp_thres,dist_thres,bat_thres)
    control1=Control()

    len_queue=queue.Queue(maxsize=max_q_len)
    pro_queue=queue.Queue(maxsize=max_q_len)
    stop_event=threading.Event()

    t_sensor=threading.Thread(target=sensor_producer,args=(sensor1,len_queue,stop_event,max_q_len))
    t_processor=threading.Thread(target=processor_consumer,args=(processor1,len_queue,pro_queue,stop_event,max_q_len))
    t_sensor.start()
    t_processor.start()

    log.info(f"机器人程序启动，最大运行时常为{max_run_time}，ctrl+c即可停止")
    start_time=time.time()

    try:
        while not stop_event.is_set():
            if time.time()-start_time>=max_run_time:
                log.info("时长已达，准备停止所有线程，退出程序")
                stop_event.set()
                break
            try:
                lastest_state=pro_queue.get(timeout=0.2)
                cmd=control1.get_cmd(lastest_state)
                log.info(f"输出控制指令{cmd}")
            except queue.Empty:
                continue
    except KeyboardInterrupt:
        log.info("用户输入ctrl+c，准备停止所有线程，退出程序")
        stop_event.set()
    finally:
        t_sensor.join()
        t_processor.join()
        log.info("所有线程停止完毕，程序正常结束")       




