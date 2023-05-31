import platform
from utils.jsontools import *

def config():
    conf = parse_json("config.json")
    if conf["driver_path"]=="":
        if platform.system()=="Windows":
            conf["driver_path"] = "drivers/chromedriver.exe"
        elif platform.system()=="Darwin":
            conf["driver_path"] = "/usr/local/bin/chromedriver"
        else:
            conf["driver_path"] = "/usr/bin/chromedriver"
        write_json("config.json", conf)
    else:
        pass
    return conf

