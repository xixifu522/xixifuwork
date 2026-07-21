def processor_test(x):
    print("正在处理数据")
    temp=x["tem"]
    if temp > 25:
        res="高温反常"
    else:
        res="温度正常"
    print(f"小车温度是{res}")
    return res