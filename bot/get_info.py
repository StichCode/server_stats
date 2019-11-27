from datetime import datetime, timedelta
from operator import itemgetter

import psutil


def __get_ram():
    """Method for getting ram system"""
    result = []
    attrs = ['pid', 'memory_percent', 'name', 'cmdline', 'cpu_times',
             'create_time', 'memory_info', 'status', 'nice', 'username']
    for proc in psutil.process_iter(attrs=attrs):
        time_start = datetime.fromtimestamp(proc.create_time())
        result.append({
            "pid": proc.pid,
            "name": proc.name(),
            "ram": proc.memory_percent(),
            "cmd line": proc.cmdline(),
            "status": proc.status(),
            "start time": time_start.strftime('%d-%m-%Y %H:%M:%S'),
            "time works": str(timedelta(seconds=(datetime.now() - time_start).total_seconds()))
        })
    return result


def get_cpy_percent(pid, interval=0.0):
    """ (-__-) """
    process = psutil.Process(pid)
    return {"cpu": process.cpu_percent(interval=interval)}


def memory_usage():
    memory_disk = dict()
    disk = psutil.disk_usage('/')
    memory_disk["Memory"] = {
        "total": disk.total / (1024.0 ** 3),
        "used": disk.used / (1024.0 ** 3),
        "free": disk.free / (1024.0 ** 3),
        "%": disk.percent
    }
    return memory_disk


def prepare_data():
    text_ram = "____________RAM____________"
    for line in sorted(__get_ram(), key=itemgetter("ram"), reverse=True)[:5]:
        text_ram += "\n"
        text_ram += f"Pid        : {line['pid']}\n"
        text_ram += f"Ram        : {round(line['ram'], 2)}%\n"
        text_ram += f"Name       : {line['name']}\n"
        text_ram += f"Cmd line   : {line['cmd line'][:2]}\n"
        text_ram += f"Time works : {line['time works']}\n"
        text_ram += "___________________________"

    return text_ram
