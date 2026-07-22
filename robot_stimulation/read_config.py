import os
import json

def load_config(path):
    if not os.path.exists("config"):
        os.mkdir("config")
    try:
        with open(path,"r",encoding="utf-8")as f:
            cfg=json.load(f)
        print("配置读取成功")
        return cfg
    except FileNotFoundError:
        print(f"错误,配置文件{path}不存在")
        return None
    except json.JSONDecodeError:
        print("文件格式损坏，语法错误")
        return None
    except Exception as e:
        print(f"未知读取错误{e}")
        return None
if __name__=="__main__":
    config=load_config("config/robot_config.json")
    if config:
        print("间隔采样",config["time_inter"])
