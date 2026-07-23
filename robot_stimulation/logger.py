import os
import logging
def loggers():
    if not os.path.exists("logs"):
        os.mkdir("logs")
    log_format="%(asctime)s-%(name)s-%(levelname)s-%(message)s"
    logging.basicConfig(level=logging.INFO,
                    format=log_format,
                    handlers=[logging.FileHandler("logs/robot_run.log",encoding="utf-8"),
                             logging.StreamHandler()])
    return logging