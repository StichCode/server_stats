import subprocess
from datetime import datetime, timedelta
from operator import itemgetter

import psutil
from loguru import logger

from src.functions.message_template import template_info, get_body


def ram_cpu():
    processes_info = []

    for line in sorted(__get_info(), key=itemgetter("ram"), reverse=True)[:5]:
        processes_info.append({
                **line,
                "cpu": psutil.Process(line['pid']).cpu_percent(0.5),
                # делаем это тут, потому что занимает много времени
        })
    logger.info("Prepared dict completed")

    completed_body_string = ""

    for d in processes_info:
        completed_body_string += "\n{0} \n{1}".format("* " * 5, get_body(d))

    result = template_info("RAM and CPU", body=completed_body_string)
    logger.info(result)
    return result


def __get_info():
    """ Получаем информацию из psutil с некоторой обработкой сразу в dict"""
    result = []
    attrs = ['pid', 'memory_percent', 'name', 'cmdline', 'cpu_times',
             'create_time', 'memory_info', 'status', 'nice', 'username']
    for proc in psutil.process_iter(attrs=attrs):
        time_start = datetime.fromtimestamp(proc.create_time())
        result.append({
            "pid": proc.pid,
            "name": proc.name(),
            "ram": f"{round(proc.memory_percent(), 2)} %",
            "cmd line": proc.cmdline()[:2],
            "status": proc.status(),
            "start time": time_start.strftime('%d-%m-%Y %H:%M:%S'),
            "time works": str(timedelta(seconds=(datetime.now() - time_start).total_seconds())).split('.')[0]
        })
    logger.info(f"Get info about {len(result)} processes")
    return result


def memory_usage():
    """ Получаем информацию об использовании памяти """
    disk = psutil.disk_usage('/')

    fields = {
        "Total": f"{round(disk.total / (1024.0 ** 3), 3)} GiB",
        "Used": f"{round(disk.used / (1024.0 ** 3), 3)} GiB",
        "Free": f"{round(disk.free / (1024.0 ** 3), 3)} GiB",
        "Percent": f"{round(disk.percent, 3)} %"
    }
    result = template_info("Memory usage", fields)
    logger.info(result)
    return result


def check_connections():
    """ Кто залогинен на сервере """
    output = subprocess.check_output("w")
    return output.decode()