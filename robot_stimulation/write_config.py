import json

config_content={
    "time_inter":2,
    "temp_thres":25,
    "dist_thres":3,
    "bat_thres":65
}

with open("config/robot_config.json", "w", encoding="utf-8") as f:
    json.dump(config_content, f, indent=4, ensure_ascii=False)

print("配置文件完成")