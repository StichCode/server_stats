from datetime import datetime, timedelta

import psutil


def get_ram():
    """Method for getting ram system"""
    result = dict()
    attrs = ['pid', 'memory_percent', 'name', 'cmdline', 'cpu_times',
             'create_time', 'memory_info', 'status', 'nice', 'username']
    for proc in psutil.process_iter(attrs=attrs):
        time_start = datetime.fromtimestamp(proc.create_time())
        result[proc.pid] = {
            "name": proc.name(),
            "ram %": proc.memory_percent(),
            "cmd line": proc.cmdline(),
            "status": proc.status(),
            "start time": time_start.strftime('%d-%m-%Y %H:%M:%S'),
            "time works": str(timedelta(seconds=(datetime.now() - time_start).total_seconds()))
        }
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
