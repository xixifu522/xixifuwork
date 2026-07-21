from robot.control import  control_test
from robot.processor import processor_test
from robot.sensor import sensor_test

if __name__ == "__main__":
    print("机器人启动")
    data = sensor_test()
    stat = processor_test(data)
    action = control_test(stat)
    print("运行结束")


