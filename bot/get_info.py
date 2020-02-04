import subprocess
from datetime import datetime, timedelta
from operator import itemgetter

import psutil

from bot.templates import Template_info_system


def __get_info():
    """Method for getting all info about system"""
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


def memory_usage():
    """ Return info about message usage system"""
    disk = psutil.disk_usage('/')
    return f"Total   : {round(disk.total / (1024.0 ** 3), 3)} GiB\n" \
           f"Used    : {round(disk.used / (1024.0 ** 3), 3)} GiB\n" \
           f"Free    : {round(disk.free / (1024.0 ** 3), 3)} GiB\n" \
           f"Percent : {round(disk.percent, 3)} %\n"


def ram_cpu():
    result = []
    for line in sorted(__get_info(), key=itemgetter("ram"), reverse=True)[:5]:
        result.append([str(line['pid']), str(round(line['ram'], 2)), str(line['name']),
                       str(line['time works']).split('.')[0], str(line['cmd line'][:2]),
                       str(psutil.Process(line['pid']).cpu_percent(0.5))])
    return Template_info_system(result)


def check_connections():
    """ Check who login in to server """
    output = subprocess.check_output("w")
    return output.decode()
