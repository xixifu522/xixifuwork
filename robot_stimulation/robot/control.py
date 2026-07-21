def control_test(y):
    if "反常" in y:
        cmd = ("停车")
    else:
        cmd = ("继续开车")
    print(f"当前小车应该{cmd}")
    return cmd